import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import style 

style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)

monthly_precipitation = df.groupby('Month')['Total Precip (mm)'].mean().reset_index()
months = monthly_precipitation['Month']
avg_precip = monthly_precipitation['Total Precip (mm)']

plt.figure()
ax = plt.gca() 

bars = ax.bar(months, avg_precip, align='center', color='tab:blue')

for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2.0, 
        height,                               
        f'{height:.1f}',                     
        ha='center',                          
        va='bottom',                          
        fontsize=9,
        color='tab:gray'
    )

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(months)
ax.set_xticklabels(month_names)

ax.set_xlabel('Month')
ax.set_ylabel('Average Total Precipitation (mm)')
ax.set_title("Average Monthly Precipitation in St. John's A")

ax.set_ylim(0, avg_precip.max() * 1.15)
ax.grid(False)

plot_output_filename = os.path.join(output, 'plot_2_monthly_precip_bar.pdf')
plt.savefig(plot_output_filename)
print(f"Plot saved as {plot_output_filename}")