from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(..., min_length=4, max_length=8)