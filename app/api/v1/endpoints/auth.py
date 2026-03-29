from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import UserRegister, UserLogin
from app.services.auth_service import AuthService
from app.api.deps import get_db

router = APIRouter()


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        auth_service = AuthService(db)
        created_user = auth_service.register_user(
            username=user.username, email=user.email, password=user.password
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"Username": user.username, "is_registered": True}
