import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def corr_matrix():
  df = pd.read_csv('data/cleaned_data.csv')
  
  # Correlation Matrix
  subset_df = df[['comparing_focus_group', 'to_reference_group',
                  'focus_prevalence_num', 'reference_prevalence_num', 'disparity_value_num']]
  
  subset_encoded = pd.get_dummies(subset_df, columns=['comparing_focus_group', 'to_reference_group'], drop_first=True)
  
  new_cols = []
  for col in subset_encoded.columns:
      if col.startswith('comparing_focus_group_'):
          new_cols.append('focus_' + col.replace('comparing_focus_group_', ''))
      elif col.startswith('to_reference_group_'):
          new_cols.append('ref_' + col.replace('to_reference_group_', ''))
      else:
          new_cols.append(col)
  
  subset_encoded.columns = new_cols
  cor_matrix = subset_encoded.corr()
  
  # Keep only "strong" correlations above threshold
  threshold = 0.2
  strong_cor = cor_matrix.where(cor_matrix.abs() > threshold)
  
  # Remove columns and rows with all NaN (i.e., no strong correlations)
  cols_to_keep = strong_cor.columns[strong_cor.notna().any()]
  strong_cor_clean = strong_cor.loc[cols_to_keep, cols_to_keep]
  
  # Split visual in half
  mask = np.triu(np.ones_like(cor_matrix, dtype=bool))
  
  strong_cor = cor_matrix[cor_matrix.abs() > 0.2]
  plt.figure(figsize=(14, 10))
  sns.set(font_scale=1.1)
  sns.heatmap(strong_cor_clean, mask=mask, cmap='coolwarm', center=0)
  plt.title("Strong Correlation Matrix")
  plt.show()
