from app.db.psql import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Enum as SQLAlchemyEnum,
    Float,
    Integer,
    String,
    CheckConstraint,
    DateTime,
)
from app.models.gender import Gender
from app.models.activity_level import ActivityLevel
from app.models.diet_phase import DietPhase
from datetime import datetime


class UserInfo(Base):
    """
    Represents a user in the system with personal and health-related attributes.

    This model stores identity, physical measurements, lifestyle indicators, and
    nutritional phase data for TDEE (Total Daily Energy Expenditure) tracking.

    Table: users

    Attributes
    ----------
    id : int
        Primary key identifier for the user.

    given_name : str
        The user's first name.

    family_name : str
        The user's last name.

    email : str
        The user's email address (must be unique).

    password : str
        The hashed password for authentication.

    weight : float
        The user's body weight in kilograms.

    height : int
        The user's height in centimeters.

    age : int
        The user's age in years.

    gender : Gender
        Enum indicating male or female.

    activity_level : ActivityLevel
        Enum describing the user's physical activity level.

    tdee : float
        Total Daily Energy Expenditure calculated from the user's profile.

    diet_phase : DietPhase
        Enum representing the current nutritional phase (e.g., maintenance, bulking, cutting).

    created_at : datetime
        Timestamp when the user was created.

    updated_at : datetime
        Timestamp when the user's data was last updated.

    Relationships
    -------------
    scale_reports : List[ScaleReport]
        One-to-many relationship with `ScaleReport`. All reports are deleted if the user is deleted.

    Constraints
    -----------
    - weight must be between 40 and 200 kg
    - height must be between 130 and 220 cm
    - age must be between 10 and 120 years
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    given_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)  # Will store hashed password
    weight = Column(Float, nullable=False)
    height = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(SQLAlchemyEnum(Gender), nullable=False)
    activity_level = Column(SQLAlchemyEnum(ActivityLevel), nullable=False)
    tdee = Column(Float, default=0.0)
    diet_phase = Column(SQLAlchemyEnum(DietPhase), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    scale_reports = relationship(
        "ScaleReport", back_populates="user", cascade="all, delete-orphan"
    )

    # Constraints
    __table_args__ = (
        CheckConstraint("weight > 40 AND weight < 200", name="check_weight_range"),
        CheckConstraint("height > 130 AND height < 220", name="check_height_range"),
        CheckConstraint("age > 10 AND age < 120", name="check_age_range"),
    )
