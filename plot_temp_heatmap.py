import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import style

style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)

temp_grid = df.pivot_table(
    index='Year', 
    columns='Month', 
    values='Mean Temp (°C)'
)

temp_data = temp_grid.values
years = temp_grid.index
months = temp_grid.columns

plt.figure(figsize=(10, 12)) 
ax = plt.gca()

im = ax.imshow(
    temp_data,
    cmap='coolwarm', 
    vmin=np.nanmin(temp_data), 
    vmax=np.nanmax(temp_data),
    origin="lower",
    interpolation='nearest', 
    extent=[months.min()-0.5, months.max()+0.5, 
            years.min()-0.5, years.max()+0.5],
    aspect='auto' 
)

cbar = plt.colorbar(im, ax=ax, pad=0.02)
cbar.set_label(r'Mean Temp ($^\circ$C)')

ax.set_xlabel('Month')
ax.set_ylabel('Year')

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(months)
ax.set_xticklabels(month_names, rotation=45)

year_ticks = years[::5] 
ax.set_yticks(year_ticks)
ax.set_yticklabels(year_ticks)

ax.set_title("Monthly Mean Temperature 'Fingerprint' (1942-2011)")

ax.grid(False)

plot_output_filename = os.path.join(output, 'plot_5_temp_heatmap.pdf')
plt.savefig(plot_output_filename)
print(f"Plot saved as {plot_output_filename}")
