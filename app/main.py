from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.api.deps import get_db

app = FastAPI(title="LifeOS")


@app.get("/")
def root(db: Session = Depends(get_db)):
    return {
        "status": "ok",
        "db_connected": str(db is not None)
    }