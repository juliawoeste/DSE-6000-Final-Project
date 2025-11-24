import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt

def top_ten_groups():
  df = pd.read_csv('data/cleaned_data.csv')
  
  sd_by_focus = df.groupby('comparing_focus_group')['disparity_value_num'].mean().sort_values(ascending=False).head(10)

  sns.set_theme(style="whitegrid", font_scale=1.25)
  plt.figure(figsize=(12, 7))

  palette = sns.color_palette("rocket_r", len(sd_by_focus))


  sd_focus_plot = sd_by_focus.plot.bar(color=palette, edgecolor='black', title='Top 10 Groups by Average Smoking Disparities')
  sd_focus_plot.set_ylabel('Average Smoking Disparity')
  sd_focus_plot.set_xlabel('Comparing Focus Group')

  for i, v in enumerate(sd_by_focus):
      sd_focus_plot.text(
          i,
          v + (0.02 * sd_by_focus.max()),
          f"{v:.2f}",
          ha="center",
          va="bottom",
          fontsize=12,
          fontweight='bold'
      )

  plt.xticks(rotation=45, ha='right')
  sd_focus_plot.grid(axis='y', linestyle='--', alpha=0.6)

  plt.tight_layout()
  plt.show()
