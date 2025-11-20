import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import plotly.express as px

def top10_lowest_avg_disparity():
    df = pd.read_csv('data/cleaned_data.csv')
    
    state_avg = df.groupby("state")["disparity_value_num"].mean().reset_index()

    # 10 lowest states
    lowest10 = state_avg.nsmallest(10, "disparity_value_num")
    lowest10 = lowest10.sort_values("disparity_value_num", ascending=True)

    fig = px.bar(
        lowest10,
        x="state",
        y="disparity_value_num",
        title="Top 10 States with the Lowest Average Smoking Disparity",
        labels={
            "state": "State",
            "disparity_value_num": "Average Smoking Disparity"
        },
        color="disparity_value_num", 
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        coloraxis_showscale=False
    )

    return fig
