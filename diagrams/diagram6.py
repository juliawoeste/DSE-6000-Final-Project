import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import plotly.express as px


def facet_line_disparity_by_demographic():
    """
    Facet line chart:
    - One subplot per demographic group
    - x = year
    - y = mean disparity_value_num
    """
    df = pd.read_csv("data/cleaned_data.csv")

    # Mean disparity per year and demographic across all states / focus groups
    grouped = (
        df.groupby(["year", "demographic"])["disparity_value_num"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        grouped,
        x="year",
        y="disparity_value_num",
        facet_col="demographic",
        facet_col_wrap=3,
        markers=True,
        title="Average Smoking Disparity Over Time by Demographic Group",
        labels={
            "year": "Year",
            "disparity_value_num": "Average Smoking Disparity (Disparity Value)",
            "demographic": "Demographic Group",
        },
    )

    # Make layout clean and readable
    fig.update_layout(
        hovermode="x unified",
        margin=dict(l=40, r=40, t=80, b=40),
    )

    # Cleaner facet titles & yearly ticks
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.update_xaxes(dtick=1)

    return fig