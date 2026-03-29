from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.db = session

    def get_user_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()


    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()


    def create_user(self, username: str, email: str, hashed_password: str):
        user = User(username=username, email=email, hashed_password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user