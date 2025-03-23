from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FoodItemResponse(BaseModel):
    """
    Response model for a stored food item.

    This model is used to return food items from the API, with values per 100 grams
    and optional package information.
    """

    id: int
    name: str

    # Nutrition per 100g
    calories: float
    protein: float
    fat: float
    carbohydrates: float
    fiber: float
    sugar: float
    sodium: float

    # Optional for package info
    package_amount: Optional[float] = None
    serving_size: Optional[float] = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
