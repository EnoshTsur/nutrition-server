from app.db.psql import Base
from sqlalchemy import Column, Float, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class UserMacros(Base):
    """
    Represents a macro target plan for a specific user based on their goal and TDEE.

    This is updated each time the user's diet phase or body changes.
    """

    __tablename__ = "user_macro_plans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    # Target macros (per day)
    target_calories = Column(Float, nullable=False)
    target_protein = Column(Float, nullable=False)
    target_fat = Column(Float, nullable=False)
    target_carbohydrates = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Optional: backref to user if needed
    user = relationship("UserInfo")
