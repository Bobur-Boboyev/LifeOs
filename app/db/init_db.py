from app.db.session import engine
from app.db.base import Base

# import all models
from app.models import user, goal, habit, habit_log


def init_db():
    Base.metadata.create_all(bind=engine)