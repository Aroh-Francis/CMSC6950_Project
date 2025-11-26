import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import style
import os

style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)
df_baseline = df[(df['Year'] >= 1942) & (df['Year'] <= 1971)]
percentiles_10_90 = df_baseline.groupby('Month')['Mean Temp (°C)'].quantile([0.1, 0.9]).unstack()
percentiles_10_90.columns = ['q_10', 'q_90']
percentiles_05_95 = df_baseline.groupby('Month')['Mean Temp (°C)'].quantile([0.05, 0.95]).unstack()
percentiles_05_95.columns = ['q_05', 'q_95']

df = pd.merge(df, percentiles_10_90, on='Month', how='left')
df = pd.merge(df, percentiles_05_95, on='Month', how='left')
df['hot_10'] = df['Mean Temp (°C)'] > df['q_90']
df['cold_10'] = df['Mean Temp (°C)'] < df['q_10']
df['hot_05'] = df['Mean Temp (°C)'] > df['q_95']
df['cold_05'] = df['Mean Temp (°C)'] < df['q_05']

annual_counts = df.groupby('Year')[['hot_10', 'cold_10', 'hot_05', 'cold_05']].sum().reset_index()

plt.figure(figsize=(15, 7))
ax2 = plt.gca()

ax2.plot(
    annual_counts['Year'],
    annual_counts['hot_05'],
    label='Very Hot (> 95th %ile)',
    linestyle='--'
)
ax2.plot(
    annual_counts['Year'],
    annual_counts['cold_05'],
    label='Very Cold (< 5th %ile)',
    linestyle='--'
)

ax2.set_xlabel('Year')
ax2.set_ylabel('Annual Count of Extreme Months')
ax2.set_title('Sensitivity to Extreme Temperature Definition')
ax2.legend()
ax2.grid(True)

plot_output_filename = os.path.join(output, 'plot_9_extreme_sensitivity_line.pdf')
plt.savefig(plot_output_filename)
print(f"Plot is saved as {plot_output_filename}")