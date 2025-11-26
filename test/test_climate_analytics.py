import pytest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal, assert_series_equal
from climate_analytics import calculate_gdd, calculate_annual_gdd

def test_calculate_gdd_basic():
    '''Tests the core GDD calculation, similar to tests in test_array_stats_pytest.py'''
    temps = [5, 12, 18, -2]
    base = 10
    expected = np.array([0, 2, 8, 0])
    result = calculate_gdd(temps, base)   
    assert np.array_equal(result, expected)

def test_calculate_gdd_all_below():
    '''Tests for a case where no temps exceed the base cases'''
    temps = [2, 4, 6, 8]
    base = 10
    expected = np.array([0, 0, 0, 0])
    result = calculate_gdd(temps, base)
    assert np.array_equal(result, expected)

def test_calculate_gdd_empty():
    '''Tests for an an empty input'''
    temps = []
    base = 10
    expected = np.array([])
    result = calculate_gdd(temps, base)
    assert np.array_equal(result, expected)

@pytest.fixture
def sample_climate_data():   
    data = {
        'Year': [2000, 2000, 2000, 2001, 2001, 2001],
        'Month': [1, 2, 3, 1, 2, 3],
        'Mean Temp (°C)': [8, 12, 20, 9, 11, 15] 
    }
    return pd.DataFrame(data)

def test_calculate_annual_gdd(sample_climate_data):
    '''
    This is an integration test for our main function.
    
    '''
    base = 10 
    expected_data = {
        'Year': [2000, 2001],
        'Total GDD': [12, 6]
    }
    expected_df = pd.DataFrame(expected_data)    
    result_df = calculate_annual_gdd(sample_climate_data, base)    
    assert_frame_equal(result_df, expected_df)

def test_calculate_annual_gdd_missing_cols():
    '''A function to test that the function raises an error for bad data'''
    bad_df = pd.DataFrame({'Year': [2000], 'Not_Temp': [10]}) 
    with pytest.raises(ValueError):
        calculate_annual_gdd(bad_df, 10)