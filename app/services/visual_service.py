from io import BytesIO
import base64
import matplotlib.pyplot as plt
import pandas as pd


def weight_graph_to_html(df: pd.DataFrame) -> str:
    """
    Converts a user's weight DataFrame into an HTML page with an embedded line chart.

    This function uses a base64-encoded image of the weight progress graph
    (generated via matplotlib) and embeds it in an HTML template.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame containing user scale reports. Must include 'scale_date' and 'weight' columns.

    Returns
    -------
    str
        An HTML string containing the weight graph as an inline base64-encoded PNG image.
    """
    image_base64 = create_weight_graph_base64(df)
    return f"""
    <html>
        <head><title>User Weight Graph</title></head>
        <body>
            <h2>Weight Progress</h2>
            <img src="data:image/png;base64,{image_base64}" alt="Weight Graph"/>
        </body>
    </html>
    """


def create_weight_graph_base64(df: pd.DataFrame) -> str:
    """
    Generates a line plot of weight over time and returns it as a base64 string.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'scale_date' and 'weight' columns.

    Returns
    -------
    str
        Base64-encoded PNG image string.
    """
    df = df.sort_values("scale_date")

    # Set dark theme
    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        df["scale_date"],
        df["weight"],
        color="lime",
        marker="o",
        markerfacecolor="cyan",
        markeredgecolor="cyan",
    )

    # Axis and title styling
    ax.set_title("Weight Progress Over Time", color="white")
    ax.set_xlabel("Date", color="white")
    ax.set_ylabel("Weight (kg)", color="white")
    ax.grid(True, color="gray", linestyle="--", linewidth=0.5)

    # Format dates to strings for readable labels
    dates = df["scale_date"].dt.strftime("%Y-%m-%d")  # or include time if needed

    ax.set_xticks(df["scale_date"])
    ax.set_xticklabels(dates, rotation=90, ha="right", color="white")
    # Rotate x-axis labels for clarity
    plt.yticks(color="white")

    # Tight layout to prevent clipping
    plt.tight_layout()

    # Save to buffer
    buf = BytesIO()
    fig.savefig(buf, format="png", facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    return image_base64
