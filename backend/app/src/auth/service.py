import uuid
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.security import get_password_hash, verify_password
from src.users.models import User
from app.src.users import service as users_service
from app.src.users.schemas import UserCreate, UserUpdate


async def authenticate(session: AsyncSession, email: str, password: str) -> User | None:
    """Authenticate and return a user."""
    user = await users_service.get_user_by_email(session=session, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user