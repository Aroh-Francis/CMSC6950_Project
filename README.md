# St. John's A Station Climate Data Analysis

## Project Overview
This project performs a comprehensive data processing and analysis of historical climate data from the St. John's A station. The analysis focuses on identifying long-term temperature trends, precipitation patterns, and changes in extreme weather events over a 70-year period (1942-2012).

## Key Findings
Based on the analysis of the dataset:
*   **Warming Trend**: There is a clear and statistically significant warming trend at the St. John's A station.
*   **Distributional Shift**: The temperature distribution has shifted, with recent decades (2002-2022) being noticeably warmer than the baseline (1942-1962).
*   **Seasonal Consistency**: Warming is observed across all four seasons (Winter, Spring, Summer, Fall).
*   **Extreme Events**: There has been a reversal in extreme events. The early record was dominated by "Extreme Cold" months, while recent years are dominated by "Extreme Hot" months.
*   **Growing Degree Days (GDD)**: There is a persistent upward trend in GDD, indicating more heat available for growth.
*   **Precipitation**: Unlike temperature, there is no clear long-term trend in total annual precipitation, which is characterized by high year-to-year variability.

## Project Structure
The project is organized as follows:

*   **`data/`**: Contains the climate data files.
    *   `en_climate_monthly_NL_8403506_1942-2012_P1M.csv`: Raw monthly climate data.
    *   `cleaned_climate_file.csv`: Processed dataset used for the analysis.
*   **`test/`**: Contains custom analytical functions and unit tests.
    *   `climate_analytics.py`: Module containing the `calculate_annual_gdd` function for computing Growing Degree Days.
    *   `test_climate_analytics.py`: Unit tests to ensure the accuracy of the analytical functions.
    *   `plot_gdd_trend.py`: Script to plot the GDD trend.
*   **`statistics/`**: Scripts for statistical analysis.
    *   `extreme_counts.py`: Computes statistics regarding extreme values (e.g., days above/below historical means).
    *   `extreme_sensitivity.py`: Explores the sensitivity of results to the definition of "extreme values".
*   **`output/`**: Directory where generated plots are saved.
*   **Root Directory**: Contains the main plotting scripts and project configuration.

## Installation
1.  Clone this repository.
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Generating Plots
The project includes several scripts to visualize the data. Run these from the root directory to generate plots in the `output/` folder:

*   `python plot_annual_temp.py`: Plots the annual mean temperature time series.
*   `python plot_climate_shift.py`: Visualizes the shift in temperature distribution between two 20-year periods.
*   `python plot_seasonal_grid.py`: Shows mean temperature trends across all four seasons.
*   `python plot_temp_range.py`: Analyzes the trend in daily temperature ranges (Mean Max vs. Mean Min).
*   `python plot_temp_snow_dual.py`: Compares temperature trends with snowfall.
*   `python plot_monthly_precip.py`: Shows average monthly precipitation.
*   `python plot_temp_heatmap.py`: Generates a heatmap of temperatures.

### 2. Statistical Analysis
To run the statistical analysis on extreme values:

*   `python statistics/extreme_counts.py`
*   `python statistics/extreme_sensitivity.py`

### 3. Running Tests
To verify the correctness of the custom functions (e.g., GDD calculation), run the test suite using `pytest`:

```bash
pytest test/
```

## Data Source
The data used in this analysis is from the St. John's A station, covering the period from 1942 to 2012. The raw data is stored in the `data` folder.

## Discussion
For a detailed discussion of the trends and statistical methods used, please refer to the `Question4.txt` file in the root directory.
