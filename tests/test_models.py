"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    #assert (daily_mean(test_input) == test_result).all(), "not equal"

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


@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        (
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            None,
        ),
        (
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            None,
        ),
        (
            [[float('nan'), 1, 1], [1, 1, 1], [1, 1, 1]],
            [[0, 1, 1], [1, 1, 1], [1, 1, 1]],
            None,
        ),
        (
            [[1, 2, 3], [4, 5, float('nan')], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.8, 1, 0], [0.78, 0.89, 1]],
            None,

        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
        (
            0.001,
            0.00,
            ValueError,
        ),

        (
            [[-1, 2, 3,4, 5, 6,7, 8, 9]],
            0.00,
            ValueError,
        ),


    ])

def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            if isinstance(test, list):
                npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
            else:
                npt.assert_almost_equal(patient_normalise(test), expected, decimal=2)

    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
