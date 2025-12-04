import pandas as pd
import os
import matplotlib.pyplot as plt
import style

style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)
WINTER_MONTHS = [12, 1, 2]
SPRING_MONTHS = [3, 4, 5]
SUMMER_MONTHS = [6, 7, 8]
FALL_MONTHS = [9, 10, 11]


def get_seasonal_mean(df, months):
    '''This function calculates the annual mean temperature
    for a given season.'''
    seasonal_data = df[df['Month'].isin(months)]
    annual_mean = seasonal_data.groupby('Year')['Mean Temp (°C)'].mean()
    return annual_mean.reset_index()


df_winter = get_seasonal_mean(df, WINTER_MONTHS)
df_spring = get_seasonal_mean(df, SPRING_MONTHS)
df_summer = get_seasonal_mean(df, SUMMER_MONTHS)
df_fall = get_seasonal_mean(df, FALL_MONTHS)

fig, axes = plt.subplots(
    nrows=2,
    ncols=2,
    sharex=True,
    sharey=True,
    figsize=(16, 12)
)
fig.suptitle(
    "The Seasonal Mean Temperature Trends in St. John's A", fontsize=22
)
axes[0, 0].plot(
    df_winter['Year'],
    df_winter['Mean Temp (°C)'],
    'o-',
    markersize=3,
    color='tab:blue',
    label='Winter'
)
axes[0, 0].set_title('Winter (Dec, Jan, Feb)')
axes[0, 0].set_ylabel(r'Mean Temp ($^\circ$C)')
axes[0, 1].plot(
    df_spring['Year'],
    df_spring['Mean Temp (°C)'],
    'o-',
    markersize=3,
    color='tab:green',
    label='Spring'
)
axes[0, 1].set_title('Spring (Mar, Apr, May)')
axes[1, 0].plot(
    df_summer['Year'],
    df_summer['Mean Temp (°C)'],
    'o-',
    markersize=3,
    color='tab:red',
    label='Summer'
)
axes[1, 0].set_title('Summer (Jun, Jul, Aug)')
axes[1, 0].set_ylabel(r'Mean Temp ($^\circ$C)')
axes[1, 0].set_xlabel('Year')
axes[1, 1].plot(
    df_fall['Year'],
    df_fall['Mean Temp (°C)'],
    'o-',
    markersize=3,
    color='tab:orange',
    label='Fall'
)
axes[1, 1].set_title('Fall (Sep, Oct, Nov)')
axes[1, 1].set_xlabel('Year')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plot_output_filename = os.path.join(output, 'plot_7_seasonal_grid.pdf')
plt.savefig(plot_output_filename)
print(f"Plot is saved as {plot_output_filename}")
