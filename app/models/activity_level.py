from enum import Enum


class ActivityLevel(str, Enum):
    SEDENTARY = "SEDENTARY"  # Little to no exercise, desk job
    LIGHTLY_ACTIVE = "LIGHTLY_ACTIVE"  # Light exercise/sports 1-3 days/week
    MODERATELY_ACTIVE = "MODERATELY_ACTIVE"  # Moderate exercise/sports 3-5 days/week
    VERY_ACTIVE = "VERY_ACTIVE"  # Hard exercise/sports 6-7 days/week
    EXTRA_ACTIVE = "EXTRA_ACTIVE"  # Very hard exercise, training twice a day


ACTIVITY_MULTIPLIERS = {
    ActivityLevel.SEDENTARY: 1.2,
    ActivityLevel.LIGHTLY_ACTIVE: 1.375,
    ActivityLevel.MODERATELY_ACTIVE: 1.55,
    ActivityLevel.VERY_ACTIVE: 1.725,
    ActivityLevel.EXTRA_ACTIVE: 1.9,
}
