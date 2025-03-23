from typing import NamedTuple
from app.models.gender import Gender
from app.models.activity_level import ActivityLevel, ACTIVITY_MULTIPLIERS
from app.models.user_info import UserInfo


class HarrisBenedictCoefficients(NamedTuple):
    """
    NamedTuple representing the coefficients used in the Harris-Benedict equation
    for calculating Basal Metabolic Rate (BMR).

    Attributes:
        base_metabolic_rate (float): The base BMR value.
        weight_coefficient (float): Coefficient for the weight factor in BMR calculation.
        height_coefficient (float): Coefficient for the height factor in BMR calculation.
        age_coefficient (float): Coefficient for the age factor in BMR calculation.
    """

    base_metabolic_rate: float
    weight_coefficient: float
    height_coefficient: float
    age_coefficient: float


coefficient_by_gender = {
    Gender.MALE: HarrisBenedictCoefficients(88.362, 13.397, 4.799, 5.677),
    Gender.FEMALE: HarrisBenedictCoefficients(447.593, 9.247, 3.098, 4.330),
}


def calculate_bmr(
    gender: Gender,
    weight_kg: float,
    height_cm: int,
    age_years: int,
) -> float:
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.

    Args:
        gender (Gender): User's gender (MALE or FEMALE).
        weight_kg (float): Weight in kilograms.
        height_cm (int): Height in centimeters.
        age_years (int): Age in years.

    Returns:
        float: BMR in calories per day.
    """
    base, weight_coef, height_coef, age_coef = coefficient_by_gender[gender]
    return (
        base
        + (weight_coef * weight_kg)
        + (height_coef * height_cm)
        - (age_coef * age_years)
    )


def calculate_tdee(
    gender: Gender,
    weight_kg: float,
    height_cm: int,
    age_years: int,
    activity_level: ActivityLevel,
) -> float:
    """
    Calculate Total Daily Energy Expenditure based on BMR and activity level.

    Args:
        gender: User's gender (MALE or FEMALE)
        weight_kg: Weight in kilograms
        height_cm: Height in centimeters
        age_years: Age in years
        activity_level: One of "sedentary", "light", "moderate", "active", "very_active"

    Returns:
        TDEE in calories
    """
    bmr = calculate_bmr(gender, weight_kg, height_cm, age_years)

    # Get the activity multiplier from constants
    activity_multiplier = ACTIVITY_MULTIPLIERS[activity_level]

    # Calculate TDEE
    tdee = bmr * activity_multiplier

    return tdee


def calculate_user_tdee(user: UserInfo) -> float:
    """
    Calculate Total Daily Energy Expenditure based on BMR and activity level.

    Args:
        user: UserInfo

    Returns:
        TDEE in calories
    """
    return calculate_tdee(
        user.gender, user.weight, user.height, user.age, user.activity_level
    )
