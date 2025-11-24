import pandas as pd
import plotly.express as px

def top_ten_groups():
    """
    Returns a Plotly figure of the top 10 comparing focus groups
    with the highest average smoking disparity.
    """
    df = pd.read_csv('data/cleaned_data.csv')

    # Compute top 10
    sd_by_focus = (
        df.groupby('comparing_focus_group')['disparity_value_num']
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        sd_by_focus,
        x="comparing_focus_group",
        y="disparity_value_num",
        title="Top 10 Groups by Average Smoking Disparities",
        color="disparity_value_num",                 # gives a gradient similar to seaborn rocket_r
        color_continuous_scale="Rocket_r",
        text="disparity_value_num",
        labels={
            "comparing_focus_group": "Comparing Focus Group",
            "disparity_value_num": "Average Smoking Disparity",
        },
    )

    # Mirror your labels above bars
    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    # Layout styling similar to seaborn version
    fig.update_layout(
        xaxis_tickangle=-45,
        yaxis_title="Average Smoking Disparity",
        xaxis_title="Comparing Focus Group",
        margin=dict(l=40, r=40, t=80, b=80),
        coloraxis_showscale=False,   # Hide colorbar if not needed
    )

    return fig
