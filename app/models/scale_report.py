from app.db.psql import Base
from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime, CheckConstraint
from datetime import datetime
from sqlalchemy.orm import relationship


class ScaleReport(Base):
    __tablename__ = "scale_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    scale_date = Column(DateTime, nullable=False)
    weight = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("UserInfo", back_populates="scale_reports")

    # Constraints
    __table_args__ = (CheckConstraint("weight > 0", name="check_weight_positive"),)
