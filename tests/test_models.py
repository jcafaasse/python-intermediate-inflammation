"""Tests for statistics functions within the Model layer."""

import pytest
import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean, daily_max, daily_min

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0, 0], [0, 0], [0, 0]], [0, 0]),
            ([[1,2], [3, 4], [5, 6]], [3, 4])
        ]        
)

def test_daily_mean(test_input, test_result):
    """ Test that daily mean function works for given test_input and test_result"""

    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean_strings():
    """ Test for TypeError when parsing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_max(["Hello", "there"])

def test_daily_mean_single_integer():
    """ Test that mean function returns a single integer input """

    test_input = 3
    
    with npt.assert_raises(np.exceptions.AxisError):
        daily_mean(test_input)



def test_daily_max_integers():
    """Test that max function works for an array of integers."""

    test_input = np.array([[1, 2], 
                           [-3, 4], 
                           [5, 0]])
    test_result = np.array([5, 4])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_strings():
    """ Test for TypeError when parsing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_max(["Hello", "there"])

def test_daily_min_integers():
    """Test that min function works for an array of integers."""

    test_input = np.array([[1, 2], 
                           [-3, 4], 
                           [5, 0]])
    test_result = np.array([-3, 0])

    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_string():
    """ Test for TypeError when parsing string """

    with pytest.raises(TypeError):
        daily_min(["Hello", "there"])

