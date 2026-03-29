from pydantic import BaseModel, EmailStr


class UserRegisted(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    email: EmailStr
    password: str