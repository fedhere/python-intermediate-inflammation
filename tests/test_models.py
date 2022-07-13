"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_min():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_min

    test_input = np.array([[1., 2.3],
                           [-3.5, 4.0],
                           [5.5, 0.9]])
    test_result = np.array([-3.5, 0.9])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_max():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_max

    test_input = np.array([[1., 2.3],
                           [-3.5, 4.0],
                           [5.5, 0.9]])
    test_result = np.array([5.5, 4.0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)
