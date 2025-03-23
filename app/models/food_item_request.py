from pydantic import BaseModel, Field, constr, condecimal
from typing import Optional


class FoodItemRequest(BaseModel):
    """
    Request model for creating a new food item.

    Nutritional values are expected per 100 grams. Optionally,
    you can provide the total weight of a package (e.g., 200g container)
    or a serving size (e.g., 30g bar) for future consumption calculations.
    """

    name: constr(strip_whitespace=True, min_length=1) = Field(
        ..., example="Protein Shake"
    )

    # Nutrition per 100g
    calories: condecimal(ge=0) = Field(..., example=400)
    protein: condecimal(ge=0) = Field(..., example=80)
    fat: condecimal(ge=0) = Field(..., example=4)
    carbohydrates: condecimal(ge=0) = Field(..., example=12)
    fiber: Optional[condecimal(ge=0)] = Field(0.0, example=1.5)
    sugar: Optional[condecimal(ge=0)] = Field(0.0, example=1.0)
    sodium: Optional[condecimal(ge=0)] = Field(0.0, example=50)

    # Optional for packaging
    package_amount: Optional[condecimal(gt=0)] = Field(
        None, example=200
    )  # e.g., full package weight in grams
    serving_size: Optional[condecimal(gt=0)] = Field(
        None, example=30
    )  # e.g., 1 bar = 30g

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Protein Shake",
                "calories": 400,
                "protein": 80,
                "fat": 4,
                "carbohydrates": 12,
                "fiber": 1.5,
                "sugar": 1.0,
                "sodium": 50,
                "package_amount": 200,
                "serving_size": 30,
            }
        }
