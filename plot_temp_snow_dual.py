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

annual_mean_temp = df.groupby('Year')['Mean Temp (°C)'].mean()
annual_total_snow = df.groupby('Year')['Total Snow (cm)'].sum()

annual_data = pd.DataFrame({
    'Mean Temp': annual_mean_temp,
    'Total Snow': annual_total_snow
}).reset_index()

fig, ax = plt.subplots()

color_temp = 'tab:red'
ax.plot(
    annual_data['Year'], 
    annual_data['Mean Temp'], 
    color=color_temp,
    linestyle='-',
    marker='o',
    markersize=4,
    label='Mean Temp'
)
ax.set_xlabel('Year')
ax.set_ylabel(r'Annual Mean Temp ($^\circ$C)', color=color_temp)
ax.tick_params(axis='y', labelcolor=color_temp)
ax.grid(False)
ax2 = ax.twinx()
color_snow = 'tab:blue'
ax2.plot(
    annual_data['Year'], 
    annual_data['Total Snow'], 
    color=color_snow,
    linestyle='--',
    marker='s',
    markersize=4,
    label='Total Snow'
)
ax2.set_ylabel('Annual Total Snow (cm)', color=color_snow)
ax2.tick_params(axis='y', labelcolor=color_snow)
ax2.grid(False)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=2)
plt.title("Annual Temperature vs. Total Snowfall in St. John's A", pad=30)
plot_output_filename = os.path.join(output, 'plot_6_dual_axis_temp_snow.pdf')
plt.savefig(plot_output_filename)
print(f"Plot saved as {plot_output_filename}")