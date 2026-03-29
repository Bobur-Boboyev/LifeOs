from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.api.deps import get_db

from app.db.init_db import init_db
from app.api.v1.endpoints import auth

init_db()


app = FastAPI(title="LifeOS")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])


@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"status": "ok", "db_connected": str(db is not None)}
