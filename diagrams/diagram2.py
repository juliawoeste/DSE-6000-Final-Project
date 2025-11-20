import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import plotly.express as px

def smoking_disparity_vs_income(): 

    df = pd.read_csv('data/cleaned_data.csv')

    income_df = df[df['demographic'] == "Income"]

    #Average of disparity value
    grouped = (
        income_df.groupby(["year", "comparing_focus_group"])["disparity_value_num"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        grouped,
        x="year",
        y="disparity_value_num",
        color="comparing_focus_group",
        category_orders={"comparing_focus_group": ["<20000", "20000-74999", ">=75000"]},
        markers=True,
        title="Smoking Disparity by Income Over Time",
        labels={
            "year": "Year",
            "disparity_value_num": "Average Smoking Disparity",
            "comparing_focus_group": "Income Group"
        }
    )

    fig.update_layout(
        legend_title="Income Group",
        hovermode="x unified"
    )

    return fig
