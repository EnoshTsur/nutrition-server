from fastapi import APIRouter, HTTPException
from app.models import FoodItemRequest, FoodItemResponse
from app.services.food_item_service import create_and_transform_food_item
from returns.result import Failure


food_item_router = APIRouter(prefix="/food_item", tags=["food_item"])


@food_item_router.post("/create", response_model=FoodItemResponse)
def create_food_item(item: FoodItemRequest):
    """
    Create a new food item.

    This endpoint receives nutritional data per 100 grams (with optional
    package size), stores it in the database, and returns the saved food
    item as a response.

    Parameters
    ----------
    item : FoodItemRequest
        The nutritional information for the new food item.

    Returns
    -------
    FoodItemResponse
        The persisted food item with generated ID and timestamps.

    Raises
    ------
    HTTPException
        If the creation process fails (e.g., database error), returns HTTP 500.
    """
    result = create_and_transform_food_item(item)

    if isinstance(result, Failure):
        return HTTPException(status_code=500, detail=result.failure())
    return result.unwrap()
