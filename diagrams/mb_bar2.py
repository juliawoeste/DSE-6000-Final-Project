import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt

def bottom_ten_groups():
  df = pd.read_csv('data/cleaned_data.csv')
  
  sd_by_focus_low = df.groupby('comparing_focus_group')['disparity_value_num'].mean().sort_values().head(10)

  sns.set_theme(style="whitegrid", font_scale=1.25)
  plt.figure(figsize=(12, 7))

  palette = sns.color_palette("ch:s=.25,rot=-.35", len(sd_by_focus_low))

  sd_focus_plot_low = sd_by_focus_low.plot.bar(color=palette, edgecolor='black', title='Bottom 10 Groups by Average Smoking Disparities')
  sd_focus_plot_low.set_ylabel('Average Smoking Disparity')
  sd_focus_plot_low.set_xlabel('Comparing Focus Group')

  for i, v in enumerate(sd_by_focus_low):
      sd_focus_plot_low.text(
          i,
          v + (0.02 * sd_by_focus_low.max()),
          f"{v:.2f}",
          ha="center",
          va="bottom",
          fontsize=12,
          fontweight='bold'
      )
  plt.xticks(rotation=45, ha='right')
  sd_focus_plot_low.grid(axis='y', linestyle='--', alpha=0.6)
  plt.tight_layout()
  plt.show()  
