from typing import Optional
from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: Optional[str] = None

class NewPassword(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8, max_length=40) 


class GoogleToken(BaseModel):
    token: str

class GoogleLinkRequest(BaseModel):
    token: str
    password: str

class GoogleAuthResponse(BaseModel):
    access_token: str | None = None
    token_type: str | None = None
    requires_password: bool | None = None
    email: str | None = None
    google_user_id: str | None = None
    message: str | None = None