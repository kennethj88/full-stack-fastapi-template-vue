from typing import TYPE_CHECKING, List
import uuid
from sqlalchemy import Boolean, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.models import BaseModel

if TYPE_CHECKING:
    from ..items.models import Item
    from ..auth.models import SocialAccount

class User(BaseModel):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(
        String(255), 
        unique=True, 
        index=True, 
        nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, 
        default=True, 
        nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, 
        default=False, 
        nullable=False
    )
    full_name: Mapped[str | None] = mapped_column(
        String(255), 
        nullable=True
    )

    # Relationships
    items: Mapped[List["Item"]] = relationship(
        "Item", 
        back_populates="owner",
        cascade="all, delete-orphan"
    )
    social_accounts: Mapped[List["SocialAccount"]] = relationship(
        "SocialAccount",
        back_populates="user",
        cascade="all, delete-orphan"
    ) 