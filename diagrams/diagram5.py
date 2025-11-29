import pandas as pd
import plotly.express as px

def smoking_distribution_boxplot(demographic_boxplot):
    df = pd.read_csv('data/cleaned_data.csv')
    df3 = df[df['demographic'] == demographic_boxplot]


    fig = px.box(
        df3,
        x="comparing_focus_group",
        y="focus_prevalence_num",    
        color = "comparing_focus_group",
        title = f"Distribution of Smoking Prevalence by Focus Group ({demographic_boxplot})",
        labels = {
            "comparing_focus_group": "Focus Group",
            "focus_prevalence_num": "Focus Prevalence",
        }
    )
    fig.update_layout(
        height = 600,
        yaxis_title="Smoking Prevalence (%)",
        xaxis_title="Focus Group"    
    )

    return fig  




