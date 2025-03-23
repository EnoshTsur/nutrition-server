from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.services.user_service import get_user_scale_reports_df
from app.services.visual_service import create_weight_graph_base64, weight_graph_to_html
from operator import methodcaller

visual_router = APIRouter(prefix="/visual", tags=["visual"])


@visual_router.get("/reports/table/{id}", response_class=HTMLResponse)
async def get_scale_reports_dataframe_html(id: int):
    """
    Retrieve a user's weight reports as an HTML table.

    This endpoint queries all the weight entries for a specific user,
    converts the data into a Pandas DataFrame, and renders it as an HTML table.

    Parameters
    ----------
    id : int
        The ID of the user whose scale reports are requested.

    Returns
    -------
    HTMLResponse
        An HTML table representing the user's weight history,
        or a placeholder message if no data is available.
    """
    return (
        get_user_scale_reports_df(id)
        .map(methodcaller("to_html", index=False))
        .value_or("<h1>No reports for the provided id</h1>")
    )


@visual_router.get("/reports/graph/{id}", response_class=HTMLResponse)
async def get_scale_reports_graph(id: int):
    """
    Endpoint to generate a weight progress chart for a user.

    Parameters
    ----------
    id : int
        User ID to fetch weight history.

    Returns
    -------
    HTMLResponse
        A web page displaying the embedded weight graph.
    """
    return HTMLResponse(
        get_user_scale_reports_df(id)
        .map(weight_graph_to_html)
        .value_or("<h1>No sclae reports found</h1>")
    )
