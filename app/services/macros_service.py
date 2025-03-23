# TODO://fix this
def generate_macro_plan(tdee: float, weight_kg: float, diet_phase: str) -> dict:
    """
    Calculates daily macro targets based on TDEE, weight, and diet phase.

    Parameters
    ----------
    tdee : float
        The user's total daily energy expenditure.

    weight_kg : float
        The user's weight in kilograms.

    diet_phase : str
        One of: "cut", "bulk", "maintain"

    Returns
    -------
    dict
        A dictionary containing daily targets for:
        - calories
        - protein (g)
        - fat (g)
        - carbohydrates (g)
    """

    # Adjust calories based on diet phase
    if diet_phase == "cut":
        target_calories = tdee - 550
    elif diet_phase == "bulk":
        target_calories = tdee + 550
    else:
        target_calories = tdee

    # Protein: 2.0g per kg
    protein_g = weight_kg * 2.0
    protein_kcal = protein_g * 4

    # Fat: 1.0g per kg
    fat_g = weight_kg * 1.0
    fat_kcal = fat_g * 9

    # Carbs: remaining calories
    remaining_kcal = target_calories - (protein_kcal + fat_kcal)
    carbs_g = remaining_kcal / 4 if remaining_kcal > 0 else 0

    return {
        "target_calories": round(target_calories),
        "protein": round(protein_g),
        "fat": round(fat_g),
        "carbohydrates": round(carbs_g),
    }
