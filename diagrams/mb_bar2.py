import pandas as pd
import plotly.express as px

def bottom_ten_groups():
    df = pd.read_csv('data/cleaned_data.csv')

    sd_by_focus_low = (
        df.groupby('comparing_focus_group')['disparity_value_num']
        .mean()
        .sort_values()
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        sd_by_focus_low,
        x="comparing_focus_group",
        y="disparity_value_num",
        title="Bottom 10 Groups by Average Smoking Disparities",
        color="disparity_value_num",
        color_continuous_scale="IceFire",
        text="disparity_value_num",
        labels={
            "comparing_focus_group": "Comparing Focus Group",
            "disparity_value_num": "Average Smoking Disparity",
        },
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        yaxis_title="Average Smoking Disparity",
        xaxis_title="Comparing Focus Group",
        margin=dict(l=40, r=40, t=80, b=80),
        coloraxis_showscale=False,   # Hide colorbar for cleaner look
    )

    return fig
