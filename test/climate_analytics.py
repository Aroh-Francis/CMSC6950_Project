import pandas as pd
import numpy as np

def calculate_gdd(temps, base_temp):
    '''
    This function is defined to calculates the Growing Degree Days (GDD)
    for a given list or series of temperatures.
    The GDD for a single entry is given as max(0, temp - base_temp).
    
    '''   
    return np.maximum(0, np.asarray(temps) - base_temp)

