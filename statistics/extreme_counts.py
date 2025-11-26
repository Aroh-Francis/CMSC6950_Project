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
df = pd.read_csv(file_path)
df_baseline = df[(df['Year'] >= 1942) & (df['Year'] <= 1971)]

percentiles_10_90 = df_baseline.groupby('Month')['Mean Temp (°C)'].quantile([0.1, 0.9]).unstack()
percentiles_10_90.columns = ['q_10', 'q_90']

df = pd.merge(df, percentiles_10_90, on='Month', how='left')
df['hot_10'] = df['Mean Temp (°C)'] > df['q_90']
df['cold_10'] = df['Mean Temp (°C)'] < df['q_10']

annual_counts = df.groupby('Year')[['hot_10', 'cold_10']].sum().reset_index()

plt.figure(figsize=(16, 8))
ax1 = plt.gca()

ax1.bar(
    annual_counts['Year'],
    annual_counts['hot_10'],
    color='tab:red',
    label='Hot Months (> 90th %ile)'
)

ax1.bar(
    annual_counts['Year'],
    -annual_counts['cold_10'],
    color='tab:blue',
    label='Cold Months (< 10th %ile)'
)

ax1.axhline(0, color='k', lw=0.8)
ax1.set_xlabel('Year')
ax1.set_ylabel('Count of Extreme Months')
ax1.set_title("Annual Count of Extreme Hot vs Cold Months (Baseline: 1942–1971)")
ax1.legend()
ax1.grid(False)

plot_output_filename = os.path.join(output, 'plot_8_extreme_counts_bar.pdf')
plt.savefig(plot_output_filename)
print(f"Plot is saved as {plot_output_filename}")