import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def corr_matrix():
    df = pd.read_csv("data/cleaned_data.csv")

    # Correlation Matrix 
    subset_df = df[['comparing_focus_group', 'to_reference_group', 'focus_prevalence_num', 'reference_prevalence_num', 'disparity_value_num']]

    subset_encoded = pd.get_dummies(subset_df, columns=["comparing_focus_group", "to_reference_group"], drop_first=True)

    # rename dummy columns to your same convention
    new_cols = []
    for col in subset_encoded.columns:
        if col.startswith("comparing_focus_group_"):
            new_cols.append("focus_" + col.replace("comparing_focus_group_", ""))
        elif col.startswith("to_reference_group_"):
            new_cols.append("ref_" + col.replace("to_reference_group_", ""))
        else:
            new_cols.append(col)

    subset_encoded.columns = new_cols

    cor_matrix = subset_encoded.corr()
    threshold = 0.2
    strong_cor = cor_matrix.where(cor_matrix.abs() > threshold)

    cols_to_keep = strong_cor.columns[strong_cor.notna().any()]
    strong_cor_clean = strong_cor.loc[cols_to_keep, cols_to_keep]

    # Keep only the lower triangle of matrix
    mask = np.triu(np.ones_like(strong_cor_clean, dtype=bool), k=1)
    masked_matrix = strong_cor_clean.mask(mask)

    fig = go.Figure(
        data=go.Heatmap(
            z=masked_matrix.values,
            x=masked_matrix.columns,
            y=masked_matrix.index,
            colorscale="RdBu",
            zmin=-1,
            zmax=1,
            hoverongaps=False,
            colorbar=dict(title="Correlation"),
        )
    )

    fig.update_layout(
        title="Strong Correlation Matrix (|r| > 0.2)",
        xaxis=dict(tickangle=45),
        margin=dict(l=80, r=80, t=80, b=80),
        height=700,
    )

    return fig
