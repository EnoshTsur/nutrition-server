from app.models import FoodItemRequest, FoodItemResponse
from app.repository.food_item_repository import create_food_item
from returns.result import Result


def create_and_transform_food_item(
    food_item: FoodItemRequest,
) -> Result[FoodItemResponse, Exception]:
    """
    Creates a new food item in the database and transforms it into a response DTO.

    Parameters
    ----------
    food_item : FoodItemRequest
        The request model containing per-100g nutritional values and optional package info.

    Returns
    -------
    Result[FoodItemResponse, Exception]
        A Result object containing either the response DTO or an exception.
    """
    return create_food_item(food_item).map(
        lambda item: FoodItemResponse.model_validate(item)
    )
