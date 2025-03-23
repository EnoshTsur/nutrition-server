from app.db.psql import psql_session
from app.models import FoodItemRequest, FoodItem
from returns.result import safe


@safe
def create_food_item(food_item: FoodItemRequest) -> FoodItem:
    """
    Persists a new food item to the database using the provided nutritional data.

    This function accepts a validated FoodItemRequest object, creates a corresponding
    FoodItem ORM instance, and commits it to the database using a SQLAlchemy session.
    It is wrapped with `@safe` from the `returns` library to capture any exceptions
    as a `Result`.

    Parameters
    ----------
    food_item : FoodItemRequest
        A Pydantic request model containing nutritional values per 100 grams,
        and optional metadata such as package amount and serving size.

    Returns
    -------
    FoodItem
        The newly created SQLAlchemy FoodItem instance with generated ID and timestamps.

    Notes
    -----
    - This function should not be called directly from FastAPI endpoints.
      Use it through the service layer which maps to a Pydantic response.
    - Any exceptions raised during the database transaction (e.g., constraint violations)
      will be wrapped in a `Failure` Result.
    """
    with psql_session() as session:
        item = FoodItem(
            name=food_item.name,
            package_amount=food_item.package_amount,
            serving_size=food_item.serving_size,
            calories=food_item.calories,
            protein=food_item.protein,
            fat=food_item.fat,
            carbohydrates=food_item.carbohydrates,
            fiber=food_item.fiber,
            sugar=food_item.sugar,
            sodium=food_item.sodium,
        )

        session.add(item)
        session.commit()
        session.refresh(item)
        return item
