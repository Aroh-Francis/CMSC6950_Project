import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import style # Import our custom style

# Apply the custom style
style.set_plot_style()
data = "data"
output = "output"

file_path = os.path.join(data, 'cleaned_climate_file.csv')
df = pd.read_csv(file_path)


# --- Data Processing ---
# Filter the data into two distinct periods as requested
df_early = df[(df['Year'] >= 1942) & (df['Year'] <= 1962)]
df_late = df[(df['Year'] >= 2002) & (df['Year'] <= 2022)]

# --- Plotting ---
# This plot is a comparative histogram, inspired by histogram.py (Day13).
# We use seaborn's histplot to easily overlay two distributions
# and their Kernel Density Estimates (KDEs).

# Set plot defaults, similar to kwargs in histogram.py
kwargs = {'kde': True,
          'bins': 25,          # Use a few more bins for detail
          'stat': 'density',   # Use density to normalize counts
          'edgecolor': 'none',
          'linewidth': 0.5,
          'alpha': 0.7,
          }

# Create a single subplot
plt.figure()
ax = plt.gca()

# Plot the "Early" data
sns.histplot(data=df_early,
             x='Mean Temp (°C)',
             color='tab:blue',
             label='1942-1962 (Early)',
             **kwargs,
             ax=ax)

# Plot the "Late" data on the same axes
sns.histplot(data=df_late,
             x='Mean Temp (°C)',
             color='tab:red',
             label='2002-2022 (Late)',
             **kwargs,
             ax=ax)

# --- Labels and Legend ---
# As in histogram.py, we set labels and a legend.
ax.set_xlabel(r'Mean Monthly Temp ($^\circ$C)') # Use LaTeX for degree symbol
ax.set_ylabel('Density')
ax.set_title("Climate Shift in St. John's A (Early vs. Late)")

# A simple legend is sufficient here
ax.legend()

# # Save the figure
# output_filename = 'plot_3_climate_shift_hist.pdf'
# plt.savefig(output_filename)

# print(f"Plot saved as {output_filename}")


plot_output_filename = os.path.join(output, 'plot_3_climate_shift_hist.pdf')
plt.savefig(plot_output_filename)
print(f"Plot saved as {plot_output_filename}")