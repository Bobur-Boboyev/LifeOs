from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepository(session=db)

    def register_user(self, username: str, email: str, password: str) -> User:
        if self.repo.get_user_by_username(username=username):
            raise ValueError("Username already exist")
        if self.repo.get_user_by_email(email=email):
            raise ValueError("Email already registered")

        hashed_pw = hash_password(password=password)

        return self.repo.create_user(
            username=username, email=email, hashed_password=hashed_pw
        )
