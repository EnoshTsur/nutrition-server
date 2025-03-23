from app.db.psql import psql_session
from returns.result import safe
from app.models import UserInfo, UserRequest, ScaleRequest, ScaleReport
from app.services.tdee_service import calculate_tdee


@safe
def create_user(user: UserRequest) -> UserInfo:
    """
    Creates a new user and stores them in the PostgreSQL database.

    This function calculates the user's TDEE based on their attributes,
    creates a new UserInfo record, and persists it in the database.

    Parameters
    ----------
    user : UserRequest
        The user's input data including name, email, weight, height, age, etc.

    Returns
    -------
    UserInfo
        The newly created user record with the TDEE calculated and included.
    """
    with psql_session() as session:
        user_to_save = UserInfo(
            given_name=user.given_name,
            family_name=user.family_name,
            email=user.email,
            password=user.password,
            weight=user.weight,
            height=user.height,
            age=user.age,
            gender=user.gender,
            activity_level=user.activity_level,
            diet_phase=user.diet_phase,
            tdee=calculate_tdee(
                user.gender, user.weight, user.height, user.age, user.activity_level
            ),
        )
        session.add(user_to_save)
        session.commit()
        session.refresh(user_to_save)
        return user_to_save


@safe
def create_scale_report(scale_request: ScaleRequest) -> ScaleReport:
    """
    Creates a new scale report entry for a given user.

    Stores the user's weight measurement along with the date
    in the ScaleReport table.

    Parameters
    ----------
    scale_request : ScaleRequest
        The input data containing user_id, scale_date, and weight.

    Returns
    -------
    ScaleReport
        The newly created scale report record.
    """
    with psql_session() as session:
        scale_to_save = ScaleReport(
            user_id=scale_request.user_id,
            scale_date=scale_request.scale_date,
            weight=scale_request.weight,
        )

        session.add(scale_to_save)
        session.commit()
        session.refresh(scale_to_save)
        return scale_to_save


@safe
def get_user_scale_report(user_id: int):
    """
    Retrieves the weight history for a specific user, sorted by date descending.

    Joins the ScaleReport and UserInfo tables to return each scale entry
    along with the user's name.

    Parameters
    ----------
    user_id : int
        The ID of the user whose scale history is to be fetched.

    Returns
    -------
    list of tuples
        Each tuple contains:
        - weight: float
        - scale_date: datetime
        - given_name: str
        - family_name: str
    """
    with psql_session() as session:
        return (
            session.query(
                ScaleReport.weight,
                ScaleReport.scale_date,
                UserInfo.given_name,
                UserInfo.family_name,
            )
            .join(UserInfo, ScaleReport.user_id == UserInfo.id)
            .filter(UserInfo.id == user_id)
            .order_by(ScaleReport.scale_date.desc())
        )
