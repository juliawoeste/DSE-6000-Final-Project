import pandas as pd
import plotly.express as px

def demographic_heatmap(selected_demographic):
    df = pd.read_csv('data/cleaned_data.csv')
    df_filtered = df[df['demographic'] == selected_demographic]

    #get average disparity per state, year
    agg = (
        df_filtered.groupby(['state', 'year'])['disparity_value_num']
        .mean()
        .reset_index()  
    )

    #create the heatmap
    fig = px.density_heatmap(
        agg,
        x='year',
        y='state',
        z='disparity_value_num',
        color_continuous_scale="Viridis",
        title=f"Average Disparity by State & Year for {selected_demographic}",
    )
 
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="State",
        height=700,
        coloraxis_colorbar_title="Disparity Value",
    )
    fig.update_xaxes(type = "category")
    fig.update_yaxes(type = "category")

    return fig