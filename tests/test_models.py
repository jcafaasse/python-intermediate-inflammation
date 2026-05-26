"""Tests for statistics functions within the Model layer."""

import pytest
import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean, daily_max, daily_min

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0, 0], [0, 0], [0, 0]], [0, 0]),
            ([[1, 2], [3, 4], [5, 6]], [3, 4])
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

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0, 0], [0, 0], [0, 0]], [0, 0]),
            ([[1, 2], [-6, 4], [5, 0]], [5, 4])
        ]        
)

def test_daily_max(test_input, test_result):
    """ Test daily_max method for given test_input and test_result """

    npt.assert_equal(daily_max(test_input), test_result)

def test_daily_max_strings():
    """ Test for TypeError when parsing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_max(["Hello", "there"])

def test_daily_max_returns_single_integer_input():
    """ Test daily_max method for single integer input """

    npt.assert_equal(daily_max(3), 3)

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0, 0], [0, 0], [0, 0]], [0, 0]),
            ([[1, 2], [-3, 4], [5, 0]], [-3, 0])
        ]        
)

def test_daily_min(test_input, test_result):
    """ Test daily_min with given test_input and test_result """

    npt.assert_equal(daily_min(test_input), test_result)

def test_daily_min_string():
    """ Test for TypeError when parsing string """

    with pytest.raises(TypeError):
        daily_min(["Hello", "there"])

def test_daily_min_returns_single_integer_input():
    """ Test daily_min with single integer input """

    npt.assert_equal(daily_min(3), 3)

