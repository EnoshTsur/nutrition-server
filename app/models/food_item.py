from app.db.psql import Base
from sqlalchemy import Column, Float, Integer, String, CheckConstraint
from datetime import datetime
from sqlalchemy.types import DateTime


class FoodItem(Base):
    """
    Represents a food item with nutritional values per 100 grams.

    Attributes
    ----------
    name : str
        The name of the food item.
    package_amount : int
        Optional total weight of the package in grams.
    serving_size : int
        Optional standard serving size in grams.
    calories, protein, fat, carbohydrates, fiber, sugar, sodium : float
        Macronutrient values per 100 grams.
    """

    __tablename__ = "food_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    package_amount = Column(Integer, nullable=True)
    serving_size = Column(Integer, nullable=True)

    # Nutritional values per 100 grams
    calories = Column(Float, nullable=False)
    protein = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)
    fiber = Column(Float, default=0.0)
    sugar = Column(Float, default=0.0)
    sodium = Column(Float, default=0.0)  # in mg

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Constraints for valid nutritional data
    __table_args__ = (
        CheckConstraint("calories >= 0", name="check_calories_positive"),
        CheckConstraint("protein >= 0", name="check_protein_positive"),
        CheckConstraint("fat >= 0", name="check_fat_positive"),
        CheckConstraint("carbohydrates >= 0", name="check_carbs_positive"),
        CheckConstraint("fiber >= 0", name="check_fiber_positive"),
        CheckConstraint("sugar >= 0", name="check_sugar_positive"),
        CheckConstraint("sodium >= 0", name="check_sodium_positive"),
        CheckConstraint(
            "package_amount IS NULL OR package_amount > 0",
            name="check_package_positive",
        ),
        CheckConstraint(
            "serving_size IS NULL OR serving_size > 0",
            name="check_serving_positive",
        ),
    )
