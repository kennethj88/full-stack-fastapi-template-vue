import uuid
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.models import BaseModel

class Item(BaseModel):
    __tablename__ = "item"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False
    )

    # Relationships
    owner: Mapped["User"] = relationship("User", back_populates="items") 