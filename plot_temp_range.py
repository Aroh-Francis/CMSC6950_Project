import os
import pandas as pd
import matplotlib.pyplot as plt
import style

style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)

x_data = df['Mean Min Temp (°C)']
y_data = df['Mean Max Temp (°C)']

plt.figure()
ax = plt.gca()

ax.plot(
    x_data,
    y_data,
    'o',
    color='tab:blue',
    markersize=4,
    alpha=0.5,
    label='Monthly Data'
)

ax.set_xlabel(r'Mean Min Temp ($^\circ$C)')
ax.set_ylabel(r'Mean Max Temp ($^\circ$C)')
ax.set_title("Temperature Range in St. John's A (Min vs. Max)")

min_temp = min(x_data.min(), y_data.min()) - 1
max_temp = max(x_data.max(), y_data.max()) + 1

ax.plot(
    [min_temp, max_temp],
    [min_temp, max_temp],
    'k--',
    label='Min = Max'
)

ax.set_xlim(min_temp, max_temp)
ax.set_ylim(min_temp, max_temp)
ax.set_aspect('equal')
ax.legend()

plot_output_filename = os.path.join(output, 'plot_4_temp_range_scatter.pdf')
plt.savefig(plot_output_filename)
print(f"Plot saved as {plot_output_filename}")
