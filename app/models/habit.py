from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base import Base


class Habit(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    frequency: Mapped[str] = mapped_column(String, default="daily")
    goal_id: Mapped[int] = mapped_column(Integer, ForeignKey("goals.id"))

    goal: Mapped["Goal"] = relationship("Goal", back_populates="habits")
    logs: Mapped[list["HabitLog"]] = relationship("HabitLog", back_populates="habit")