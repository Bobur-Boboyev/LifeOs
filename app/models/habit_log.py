from sqlalchemy import Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import date

from app.db.base import Base


class HabitLog(Base):
    __tablename__ = "habit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    habit_id: Mapped[int] = mapped_column(Integer, ForeignKey("habits.id"))
    date: Mapped = mapped_column(Date, default=date.today)
    is_done: Mapped = mapped_column(Boolean, default=False)

    habit = relationship("Habit", back_populates="logs")