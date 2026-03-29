from pydantic import BaseModel, EmailStr, Field, field_validator


class UserRegister(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    password: str = Field(min_length=8)

    @field_validator("username", "password")
    @classmethod
    def not_empty(cls, v: str):
        if not v.strip():
            raise ValueError("Cannot be empty or whitespace only")
        return v.strip()


class UserLogin(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    password: str = Field(min_length=8)

    @field_validator("username", "password")
    @classmethod
    def not_empty(cls, v: str):
        if not v.strip():
            raise ValueError("Cannot be empty or whitespace only")
        return v.strip()