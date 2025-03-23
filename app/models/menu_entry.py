from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.psql import Base


class MenuEntry(Base):
    """
    Represents a single logged food entry for a user.

    This model stores either the gram amount or number of servings consumed
    of a given food item, along with precomputed nutritional values based
    on the item's per-100g data.

    Fields
    -------
    user_id : int
        The ID of the user who logged the food.

    food_item_id : int
        The ID of the referenced FoodItem.

    amount_grams : float, optional
        The quantity of the food consumed in grams. Optional if servings are used.

    amount_servings : float, optional
        The number of servings consumed, based on the FoodItem's defined serving size.
        Optional if grams are used.

    calories : float
        The total calculated calories based on the food item's nutrition per 100g.

    protein : float
        The total calculated protein in grams.

    fat : float
        The total calculated fat in grams.

    carbohydrates : float
        The total calculated carbohydrates in grams.

    eaten_at : datetime
        The timestamp of when the food was consumed. Defaults to now.

    Notes
    -----
    The actual nutritional values (calories, protein, etc.) should be computed
    in the service layer when the entry is created, using the corresponding
    `FoodItem`'s per-100g values and either `amount_grams` or `amount_servings`.

    Example
    -------
    A user logs:
    - 200g of seitan → amount_grams = 200
    - OR 2 servings of protein shake (30g each) → amount_servings = 2

    The computed nutrients are stored directly in the model for fast access.
    """

    __tablename__ = "menu_entries"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

    food_item_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)

    amount_grams = Column(Float, nullable=True)
    amount_servings = Column(Float, nullable=True)

    # Computed values — store them for easy use in UI, charts, reports, etc.
    calories = Column(Float, nullable=False)
    protein = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)

    eaten_at = Column(DateTime, default=datetime.utcnow)

    food_item = relationship("FoodItem")
