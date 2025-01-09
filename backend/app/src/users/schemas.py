from typing import Optional, List
import uuid
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: Optional[str] = Field(None, max_length=255)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=40)

class UserRegister(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    password: str = Field(..., min_length=8, max_length=40)
    full_name: Optional[str] = Field(None, max_length=255)

class UserUpdate(UserBase):
    email: Optional[EmailStr] = Field(None, max_length=255)
    password: Optional[str] = Field(None, min_length=8, max_length=40)

class UserUpdateMe(BaseModel):
    full_name: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = Field(None, max_length=255)

class UpdatePassword(BaseModel):
    current_password: str = Field(..., min_length=8, max_length=40)
    new_password: str = Field(..., min_length=8, max_length=40)

class UserPublic(UserBase):
    id: uuid.UUID

    class Config:
        from_attributes = True

class UsersPublic(BaseModel):
    data: list[UserPublic]
    count: int 