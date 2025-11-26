import pandas as pd
import numpy as np

def calculate_gdd(temps, base_temp):
    '''
    This function is defined to calculates the Growing Degree Days (GDD)         
    '''   
    return np.maximum(0, np.asarray(temps) - base_temp)


def calculate_annual_gdd(df, base_temp):
    '''
    This function calculates the total annual GDD from a climate DataFrame.
  
    '''
    if 'Mean Temp (°C)' not in df.columns or 'Year' not in df.columns:
        raise ValueError("The DataFrame must contain 'Mean Temp (°C)' and 'Year' columns")        
    df_copy = df.copy()    
    df_copy['GDD'] = calculate_gdd(df_copy['Mean Temp (°C)'], base_temp)
    annual_gdd = df_copy.groupby('Year')['GDD'].sum().reset_index()
    annual_gdd = annual_gdd.rename(columns={'GDD': 'Total GDD'})    
    return annual_gdd