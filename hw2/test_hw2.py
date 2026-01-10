"""
CMSC 14100
Autumn 2025

Test code for Homework #2
"""
import hw2
import os
import sys

import math
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw2"

@pytest.mark.parametrize("a, x, expected",
                         [(0, 0, 0),
                          (5, 2, 12),
                          (5, 0, 0),
                          (9, 1, 10),
                          (9, -2, -20),
                          (-11, 2, -20)])
def test_add_one_and_multiply(a, x, expected):
    """
    Do a single test for Exercise 1: add_one_and_multiply
    """
    steps = [f"actual = hw2.add_one_and_multiply({a}, {x})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.add_one_and_multiply(a, x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("temp_f, prec_in, expected",
                         [(31, 0, False),
                          (25, 1.2, True),
                          (40, 5, False),
                          (32.1, 0.1, False),
                          (100.0, 10.5, False),
                          (31.9, 10, True)])
def test_is_snowing(temp_f, prec_in, expected):
    """
    Do a single test for Exercise 3: is_snowing
    """
    steps = [f"actual = hw2.is_snowing({temp_f}, {prec_in})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.is_snowing(temp_f, prec_in)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("temp_f, expected",
                         [(32, 0.0),
                          (-40, -40.0),
                          (212, 100.0),
                          (-22.5, -30.27777777777778),
                          (0.0, -17.77777777777778),
                          (100, 37.77777777777778)])
def test_convert_fahrenheit_to_celsius(temp_f, expected):
    """
    Do a single test for Exercise 2: convert_fahrenheit_to_celsius
    """
    steps = [f"actual = hw2.convert_fahrenheit_to_celsius({temp_f})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.convert_fahrenheit_to_celsius(temp_f)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_equals(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("temp_f, expected",
                         [(-10, True),
                          (0.0, False),
                          (100.0, True),
                          (-4.5, False),
                          (94.9, False),
                          (94.95, True)])
def test_is_extreme_temperature(temp_f, expected):
    """
    Do a single test for Exercise 4: is_extreme_temperature
    """
    steps = [f"actual = hw2.is_extreme_temperature({temp_f})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.is_extreme_temperature(temp_f)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



@pytest.mark.parametrize("temp_f, vel_mph, vis_mi, expected",
                         [(22, 5, 10, True),
                          (5, 10, 2, False),
                          (5, 10, 3, True),
                          (50, 40, 5, False),
                          (-20, 29.9, 4, False),
                          (-10.0, 20, 6, True),
                          (0.0, 30.1, 2.99, False),
                          (10, 30, 3, True)])
def test_can_flight_takeoff(temp_f, vel_mph, vis_mi, expected):
    """
    Do a single test for Exercise 5: can_flight_takeoff
    """
    steps = [f"actual = hw2.can_flight_takeoff({temp_f}, {vel_mph}, {vis_mi})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.can_flight_takeoff(temp_f, vel_mph, vis_mi)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("temp_f, vel_mph, expected",
                         [(30, 10, 21.248293255649617),
                          (0, 20, -21.99522271347127),
                          (50, 5, 48.217993020823954),
                          (40, 15, 31.835724640164134),
                          (20, 63, -4.609271559187146),
                          (-10, 10, -28.328726824105743),
                          (32, 5.0, 27.07593432831893)])
def test_compute_wind_chill(temp_f, vel_mph, expected):
    """
    Do a single test for Exercise 6: compute_wind_chill
    """
    steps = [f"actual = hw2.compute_wind_chill({temp_f}, {vel_mph})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.compute_wind_chill(temp_f, vel_mph)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_equals(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("temp_f, vel_mph, vis_mi, prec_in, expected",
                         [(24, 0, 5, 3, False),
                          (0, 5, 1, 0, True),
                          (100, 5, 9, 0, True),
                          (59, 12, 6.5, 0.0, False),
                          (-10, 2, 12, 0, True),
                          (40, 2, 10, 11.5, True),
                          (93.5, 30, 10, 9.9, False)])
def test_is_severe_weather(temp_f, vel_mph, vis_mi, prec_in, expected):
    """
    Do a single test for Exercise 8: is_severe_weather
    """
    steps = [f"actual = hw2.is_severe_weather({temp_f}, {vel_mph}, {vis_mi}, {prec_in})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.is_severe_weather(temp_f, vel_mph, vis_mi, prec_in)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)