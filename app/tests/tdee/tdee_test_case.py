from app.models.user_info import UserInfo
from app.models.gender import Gender
from app.models.activity_level import ActivityLevel

# List of test cases
TDEE_TEST_CASES = [
    # Test case 1: Male, 84.5kg, 174cm, 34 years, very active
    (
        UserInfo(
            weight=84.5,
            height=174,
            age=34,
            gender=Gender.MALE,
            activity_level=ActivityLevel.VERY_ACTIVE,
        ),
        3212.67,
    ),
    # Test case 2: Female, 65kg, 165cm, 28 years, moderately active
    (
        UserInfo(
            weight=65,
            height=165,
            age=28,
            gender=Gender.FEMALE,
            activity_level=ActivityLevel.MODERATELY_ACTIVE,
        ),
        2229.80,
    ),
    # Test case 3: Male, 95kg, 180cm, 45 years, sedentary
    (
        UserInfo(
            weight=95,
            height=180,
            age=45,
            gender=Gender.MALE,
            activity_level=ActivityLevel.SEDENTARY,
        ),
        2363.32,
    ),
    # Test case 4: Female, 52kg, 158cm, 22 years, extremely active
    (
        UserInfo(
            weight=52,
            height=158,
            age=22,
            gender=Gender.FEMALE,
            activity_level=ActivityLevel.EXTRA_ACTIVE,
        ),
        2513.06,
    ),
    # Test case 5: Male, 78kg, 170cm, 60 years, lightly active
    (
        UserInfo(
            weight=78,
            height=170,
            age=60,
            gender=Gender.MALE,
            activity_level=ActivityLevel.LIGHTLY_ACTIVE,
        ),
        2211.74,
    ),
]
