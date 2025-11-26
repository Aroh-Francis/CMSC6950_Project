import pandas as pd
import numpy as np

def calculate_gdd(temps, base_temp):
    '''
    This function is defined to calculates the Growing Degree Days (GDD)         
    '''   
    return np.maximum(0, np.asarray(temps) - base_temp)

