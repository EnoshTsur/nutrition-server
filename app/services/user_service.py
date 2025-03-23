from app.models import (
    UserRequest,
    UserResponse,
    ScaleRequest,
    ScaleReport,
    ScaleResponse,
)
from app.repository.user_repository import (
    create_user,
    create_scale_report,
    get_user_scale_report,
)
from returns.result import Result
from returns.maybe import maybe
import pandas as pd


@maybe
def get_user_scale_reports_df(user_id: int):
    """
    Retrieves a user's scale reports and converts them into a Pandas DataFrame.

    Parameters
    ----------
    user_id : int
        The ID of the user whose scale data is requested.

    Returns
    -------
    Optional[pd.DataFrame]
        A DataFrame containing columns: weight, scale_date, given_name, family_name.
        Returns `None` if the user has no reports or an error occurred.
    """
    return (
        get_user_scale_report(user_id)
        .map(
            lambda query: pd.DataFrame(
                query.all(),
                columns=["weight", "scale_date", "given_name", "family_name"],
            )
        )
        .value_or(None)
    )


def create_and_transform_user(user: UserRequest) -> Result[UserResponse, Exception]:
    """
    Creates a user in the database and transforms the result into a UserResponse.

    Parameters
    ----------
    user : UserRequest
        The user data to be created.

    Returns
    -------
    Result[UserResponse, Exception]
        Success containing UserResponse or Failure with an Exception.
    """
    return create_user(user).map(lambda u: UserResponse.model_validate(u))


def report_user_scale(scale_request: ScaleRequest) -> Result[ScaleReport, Exception]:
    """
    Creates a scale report and transforms the result into a ScaleResponse.

    Parameters
    ----------
    scale_request : ScaleRequest
        The scale report data provided by the user.

    Returns
    -------
    Result[ScaleReport, Exception]
        Success containing ScaleResponse or Failure with an Exception.
    """
    return create_scale_report(scale_request).map(
        lambda s: ScaleResponse.model_validate(s)
    )
