import uuid
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.security import get_password_hash, verify_password
from src.users.models import User
from src.users.schemas import UserCreate, UserUpdate


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    """Get a user by email."""
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()



async def create_user(session: AsyncSession, user_create: UserCreate) -> User:
    """Create a new user."""
    db_user = User(
        email=user_create.email,
        hashed_password=get_password_hash(user_create.password),
        full_name=user_create.full_name,
        is_superuser=user_create.is_superuser,
        is_active=user_create.is_active,
    )
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def update_user(
    session: AsyncSession, db_user: User, user_in: UserUpdate
) -> User:
    """Update a user."""
    update_data = user_in.model_dump(exclude_unset=True)
    if update_data.get("password"):
        hashed_password = get_password_hash(update_data["password"])
        del update_data["password"]
        update_data["hashed_password"] = hashed_password

    for field, value in update_data.items():
        setattr(db_user, field, value)

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user
