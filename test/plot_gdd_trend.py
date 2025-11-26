import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import style  
import climate_analytics  
style.set_plot_style()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_dir = os.path.join(project_root, "data")
output_dir = os.path.join(project_root, "output")
file_path = os.path.join(data_dir, "cleaned_climate_file.csv")
df = pd.read_csv(file_path)

BASE_TEMP = 10.0
gdd_data = climate_analytics.calculate_annual_gdd(df, BASE_TEMP)

years = gdd_data['Year']
gdd = gdd_data['Total GDD']
coeffs = np.polyfit(years, gdd, 1)
trend_line = np.polyval(coeffs, years)
slope = coeffs[0]

plt.figure()
ax = plt.gca()
ax.plot(
    years, 
    gdd,
    marker='o',
    markersize=4,
    linestyle='-',
    label='Annual GDD'
)

ax.plot(
    years, 
    trend_line,
    color='tab:red',
    linestyle='--',
    label=f'Trend (Slope: {slope:.2f} GDD/year)'
)

ax.set_xlabel('Year')
ax.set_ylabel(f'Annual Total GDD (Base {BASE_TEMP:.1f}$^\\circ$C)')
ax.set_title("The Growing Degree Days Trend in St. John's A")
ax.legend()
ax.grid(True)

from pathlib import Path
script_dir = Path(__file__).resolve().parent
plot_output_filename = script_dir / 'plot_10_gdd_trend.pdf'
plt.savefig(plot_output_filename)

print(f"Plot is saved as {plot_output_filename}")


