from pydantic import BaseModel, EmailStr, Field


class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=8, description="User's password (plain)")

class UserCreate(UserLogin):
    username: str | None = Field(None, description="User's username")
class UserOut(BaseModel):
    id: int
    username: str | None = None
    email: EmailStr
    is_admin: bool = False

    model_config = {"from_attributes": True}