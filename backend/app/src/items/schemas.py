from typing import Optional
import uuid
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=255)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: Optional[str] = Field(None, min_length=1, max_length=255)

class ItemPublic(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID

    class Config:
        from_attributes = True

class ItemsPublic(BaseModel):
    data: list[ItemPublic]
    count: int 