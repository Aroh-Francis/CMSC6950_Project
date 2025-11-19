import os
import pandas as pd
import matplotlib.pyplot as plt
import style

style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)

the_annual_mean_temp = df.groupby('Year')['Mean Temp (°C)'].mean().reset_index()
mini_year = the_annual_mean_temp['Year'].min()
maxi_year = the_annual_mean_temp['Year'].max()

plt.figure() 
plt.plot(
    the_annual_mean_temp['Year'], 
    the_annual_mean_temp['Mean Temp (°C)'],
    marker='o',        
    markersize=4,       
    linestyle='-',    
    label='Annual Mean'
)

plt.xlabel('Year')
plt.ylabel('Annual Mean Temp (°C)')
plt.title(f"Annual Mean Temperature in St. John's A ({mini_year}-{maxi_year})")
plot_output_filename = os.path.join(output, 'plot_1_annual_temp_timeseries.pdf')
plt.savefig(plot_output_filename)
print(f"Plot is saved as {plot_output_filename}")