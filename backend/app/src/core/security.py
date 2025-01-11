from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Dict

import jwt
import httpx
from passlib.context import CryptContext
import logging

logger = logging.getLogger(__name__)


async def verify_google_oauth_token(token: str) -> Optional[Dict[str, Any]]:
    """Verify Google OAuth token and return user information."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f'https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={token}'
            )
            if response.status_code == 200:
                return response.json()
            return None
    except Exception:
        return None


async def get_google_user_info(token: str) -> Optional[Dict[str, Any]]:
    """Get Google user information using OAuth token."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                'https://www.googleapis.com/oauth2/v3/userinfo',
                headers={'Authorization': f'Bearer {token}'}
            )
            if response.status_code == 200:
                return response.json()
            return None
    except Exception as e:
        logger.error(f"Error getting Google user info: {e}")
        return None

from src.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: str | int,
    expires_delta: timedelta | None = None
) -> str:
    expire = datetime.now(timezone.utc) + expires_delta if expires_delta else datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

