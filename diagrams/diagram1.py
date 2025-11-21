import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import plotly.express as px

def avg_disparity_by_demographic_bar():
    """
    Bar chart:
    - One bar per demographic group
    - y = overall mean disparity_value_num across all states / years
    """
    df = pd.read_csv("data/cleaned_data.csv")

    grouped = (
        df.groupby("demographic")["disparity_value_num"]
        .mean()
        .reset_index()
        .sort_values("disparity_value_num", ascending=False)
    )

    fig = px.bar(
        grouped,
        x="demographic",
        y="disparity_value_num",
        title="Average Smoking Disparity by Demographic Group (2011–2023)",
        labels={
            "demographic": "Demographic Group",
            "disparity_value_num": "Average Smoking Disparity (Disparity Value)",
        },
    )

    fig.update_layout(
        xaxis_tickangle=-30,
        hovermode="x",
        margin=dict(l=40, r=40, t=80, b=80),
    )

    return fig