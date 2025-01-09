import uuid
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.models import BaseModel

class SocialAccount(BaseModel):
    __tablename__ = "social_account"

    provider: Mapped[str] = mapped_column(String(50), nullable=False)
    provider_user_id: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="social_accounts")

    __table_args__ = (
        UniqueConstraint('provider', 'provider_user_id', name='uq_provider_provider_user_id'),
    ) 