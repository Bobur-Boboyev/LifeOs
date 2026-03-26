from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="LifeOS")


@app.get("/")
def root():
    return {"status": "ok", "db": settings.DB_NAME}
