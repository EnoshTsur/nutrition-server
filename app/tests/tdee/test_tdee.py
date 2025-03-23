from app.services.tdee_service import calculate_user_tdee
from app.models.user_info import UserInfo
from app.tests.tdee.tdee_test_case import TDEE_TEST_CASES
import pytest


@pytest.mark.parametrize("user_info, expected_tdee", TDEE_TEST_CASES)
def test_idk(user_info: UserInfo, expected_tdee: float):
    """
    Test the calculate_user_tdee function with various user profiles.

    This parameterized test checks if the TDEE calculation returns the expected
    results for different user profiles with varying weights, heights, ages,
    genders, and activity levels.
    """
    # Calculate actual TDEE
    actual_tdee = calculate_user_tdee(user_info)

    # Assert that calculated TDEE matches expected value within a small tolerance
    assert (
        abs(actual_tdee - expected_tdee) < 0.1
    ), f"Expected TDEE {expected_tdee}, but got {actual_tdee}"
