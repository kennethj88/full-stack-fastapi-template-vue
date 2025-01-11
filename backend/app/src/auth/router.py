import logging
from datetime import timedelta
from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from google.oauth2 import id_token
from google.auth.transport import requests
from sqlalchemy import select

from src.users import service as user_service
from . import service
from src.users.schemas import UserPublic
from src.core.schemas import Message
from src.deps import (
    AsyncSessionDep,
    CurrentUser,
    get_current_active_superuser,
    get_optional_current_user
)

from src.config import settings
from src.core import security
from src.core.security import create_access_token, get_password_hash
from src.users.models import User
from src.utils import (
    generate_password_reset_token,
    generate_reset_password_email,
    send_email,
    verify_password_reset_token,
)

from .models import SocialAccount
from .schemas import Token,NewPassword,GoogleToken, GoogleLinkRequest, GoogleAuthResponse
logger = logging.getLogger(__name__)


router = APIRouter()


@router.post("/google", response_model=GoogleAuthResponse)
async def google_auth(
    token_data: GoogleToken,
    session: AsyncSessionDep,
    current_user: User | None = Depends(get_optional_current_user),
) -> GoogleAuthResponse:
    """Authenticate or register a user with Google OAuth!"""
    try:
        # Get user info from Google
        credentials = await security.get_google_user_info(token_data.token)
        if not credentials:
            raise HTTPException(status_code=400, detail="Invalid token or failed to get user info")
            
        # Extract user info from credentials
        google_user_id = credentials['sub']
        email = credentials['email']
        name = credentials.get('name')
        
        logger.warning(f"Google credentials: {credentials}")
        
        # Check if social account exists
        result = await session.execute(
            select(SocialAccount).where(
                SocialAccount.provider == "google",
                SocialAccount.provider_user_id == google_user_id
            )
        )
        social_account = result.scalar_one_or_none()
        
        if social_account:
            # Social account exists - log user in
            access_token = create_access_token(str(social_account.user_id))
            return GoogleAuthResponse(access_token=access_token, token_type="bearer")
            
        # Check if email exists
        result = await session.execute(select(User).where(User.email == email))
        existing_user = result.scalar_one_or_none()
        
        if current_user:
            # User is logged in
            if existing_user and existing_user.id != current_user.id:
                raise HTTPException(
                    status_code=400,
                    detail="This Google account is linked to another user. Please log out first."
                )
            
            # Link account to current user
            social_account = SocialAccount(
                provider="google",
                provider_user_id=google_user_id,
                user_id=current_user.id,
                email=email
            )
            session.add(social_account)
            await session.commit()
            
            return GoogleAuthResponse(message="Google account linked successfully")
            
        if existing_user:
            # Email exists but no social account - need password verification
            return GoogleAuthResponse(
                requires_password=True,
                email=email,
                google_user_id=google_user_id
            )
            
        # Create new user and social account
        user = User(
            email=email,
            full_name=name,
            is_active=True,
            hashed_password=get_password_hash(settings.SECRET_KEY[:8])  # Temporary password
        )
        session.add(user)
        await session.flush()
        
        social_account = SocialAccount(
            provider="google",
            provider_user_id=google_user_id,
            user_id=user.id,
            email=email
        )
        session.add(social_account)
        await session.commit()
        
        access_token = create_access_token(str(user.id))
        return GoogleAuthResponse(access_token=access_token, token_type="bearer")
            
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid token: {str(e)}")

@router.post("/google/link", response_model=Token)
async def link_google_account(
    request: GoogleLinkRequest,
    session: AsyncSessionDep
) -> Token:
    """Link an existing account with Google OAuth."""
    try:
        # Verify Google token
        idinfo = id_token.verify_oauth2_token(
            request.token, 
            requests.Request(), 
            settings.GOOGLE_CLIENT_ID
        )
        
        email = idinfo['email']
        google_user_id = idinfo['sub']
        
        # Verify user credentials
        result = await session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
            
        # Create social account
        social_account = SocialAccount(
            provider="google",
            provider_user_id=google_user_id,
            user_id=user.id,
            email=email
        )
        session.add(social_account)
        await session.commit()
        
        access_token = create_access_token(data={"sub": str(user.id)})
        return {"access_token": access_token, "token_type": "bearer"}
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid token: {str(e)}") 
    

@router.post("/login/access-token")
async def login_access_token(
    session: AsyncSessionDep, 
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = await service.authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=security.create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )


@router.post("/login/test-token", response_model=UserPublic)
def test_token(current_user: CurrentUser) -> Any:
    """
    Test access token
    """
    return current_user


@router.post("/password-recovery/{email}")
async def recover_password(
    email: str = Path(..., title="User email"),
    session: AsyncSessionDep = None
) -> Message:
    """
    Password Recovery
    """
    user = await user_service.get_user_by_email(session=session, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this email does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    email_data = generate_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    await send_email(
        email_to=user.email,
        subject=email_data.subject,
        html_content=email_data.html_content,
    )
    return Message(message="Password recovery email sent")


@router.post("/reset-password/")
async def reset_password(session: AsyncSessionDep, body: NewPassword) -> Message:
    """
    Reset password
    """
    email = verify_password_reset_token(token=body.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = await user_service.get_user_by_email(session=session, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this email does not exist in the system.",
        )
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(password=body.new_password)
    user.hashed_password = hashed_password
    session.add(user)
    await session.commit()
    return Message(message="Password updated successfully")


@router.post(
    "/password-recovery-html-content/{email}",
    dependencies=[Depends(get_current_active_superuser)],
    response_class=HTMLResponse,
)
async def recover_password_html_content(
    email: str, 
    session: AsyncSessionDep
) -> Any:
    """
    HTML Content for Password Recovery
    """
    user = await user_service.get_user_by_email(session=session, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    email_data = generate_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )

    return HTMLResponse(
        content=email_data.html_content, headers={"subject:": email_data.subject}
    )
