from fastapi import APIRouter
from app.models import UserRequest, UserResponse, ScaleRequest, ScaleResponse
from app.services.user_service import (
    create_and_transform_user,
    report_user_scale,
)
from typing import Optional

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post(
    "/create",
    response_model=Optional[UserResponse],
    responses={201: {"model": UserResponse}, 500: {"model": None}},
)
async def create_user_endpoint(user: UserRequest):
    """
    Create a new user.

    This endpoint receives user input, stores it in the database, calculates TDEE,
    and returns a structured response.

    Parameters
    ----------
    user : UserRequest
        The user details such as name, email, weight, height, age, etc.

    Returns
    -------
    Optional[UserResponse]
        A structured response containing user details and TDEE on success,
        or `None` if an error occurred.
    """
    return create_and_transform_user(user).value_or(None)


@users_router.post(
    "/report",
    response_model=Optional[ScaleResponse],
    responses={201: {"model": ScaleResponse}, 500: {"model": None}},
)
async def report_scale_endpoint(scale_request: ScaleRequest):
    """
    Report a user's weight on a given date.

    This endpoint stores a new scale report (weight entry) in the database
    and returns a structured response.

    Parameters
    ----------
    scale_request : ScaleRequest
        The request containing user ID, scale date, and weight.

    Returns
    -------
    Optional[ScaleResponse]
        A structured response representing the scale report, or `None` if an error occurred.
    """
    return report_user_scale(scale_request).value_or(None)
