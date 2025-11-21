import plotly.express as px 
import pandas as pd


def histogram_prevalence():
    df = pd.read_csv('data/cleaned_data.csv')

    prev_df = df[['year', 'focus_prevalence_num']] 
    fig2 = px.histogram(data_frame=prev_df, x='focus_prevalence_num', facet_col='year', 
                        nbins=20, labels={'focus_prevalence_num': 'Smoker %'}, facet_col_wrap=7,
                        facet_col_spacing=.03, facet_row_spacing=.05,
                        title='Percentage of all Smokers by Year') 
    fig2.update_layout(bargap=.05)
    fig2.update_xaxes(tickangle=45) 
    return fig2