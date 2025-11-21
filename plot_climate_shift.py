import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import style


style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)
df_early = df[(df['Year'] >= 1942) & (df['Year'] <= 1962)]
df_late = df[(df['Year'] >= 2002) & (df['Year'] <= 2022)]

kwargs = {'kde': True,
          'bins': 25,          
          'stat': 'density',   
          'edgecolor': 'none',
          'linewidth': 0.5,
          'alpha': 0.7,
          }

plt.figure()
ax = plt.gca()
sns.histplot(data=df_early,
             x='Mean Temp (°C)',
             color='tab:blue',
             label='1942-1962 (Early)',
             **kwargs,
             ax=ax)

sns.histplot(data=df_late,
             x='Mean Temp (°C)',
             color='tab:red',
             label='2002-2022 (Late)',
             **kwargs,
             ax=ax)

ax.set_xlabel(r'Mean Monthly Temp ($^\circ$C)') 
ax.set_ylabel('Density')
ax.set_title("Climate Shift in St. John's A (Early vs. Late)")
ax.legend()
plot_output_filename = os.path.join(output, 'plot_3_climate_shift_hist.pdf')
plt.savefig(plot_output_filename)
print(f"Plot saved as {plot_output_filename}")