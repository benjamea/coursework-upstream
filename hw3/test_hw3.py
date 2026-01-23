"""
CMSC 14100
Winter 2026

Test code for Homework #3
"""

import os
import sys

import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw3  # noqa: E402
import helpers  # noqa: E402

MODULE = "hw3"


@pytest.mark.parametrize(
    "cur_day, prev_day, expected",
    [
        (1.0, 1.0, 1.0),
        (2.0, 1.0, 2.0),
        (2.0, 4.0, 0.5),
        (100.0, 4.0, 25.0),
        (2.0, 2.0, 1.0),
        (-2.0, 4.0, None),
        (0, 4.0, None),
    ],
)
def test_find_relative_return(cur_day, prev_day, expected):
    """
    Do a single test for Exercise 1: find_relative_return.
    """
    steps = [f"actual = hw3.find_relative_return({cur_day}, {prev_day})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.find_relative_return(cur_day, prev_day)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "cur_day, prev_day, expected",
    [
        (1.0, 1.0, 0.0),
        (2.0, 1.0, 0.0),
        (2.0, 4.0, 0.5),
        (100.0, 4.0, 0.0),
        (2.0, 2.0, 0.0),
        (1.0, 4.0, 0.75),
        (-2.0, 4.0, None),
        (0, 4.0, None),
    ],
)
def test_find_value_at_risk(cur_day, prev_day, expected):
    """
    Do a single test for Exercise 2: find_value_at_risk.
    """
    steps = [f"actual = hw3.find_value_at_risk({cur_day}, {prev_day})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.find_value_at_risk(cur_day, prev_day)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "roi, uvar, expected",
    [
        (1.1, 0.0, "AAA"),
        (1.1, 0.05, "AA"),
        (1.05, 0.0, "D"),
        (1.4, 0.2, "BB"),
        (1.4, 0.6, "C"),
        (1.15, 0.2, "D"),
        (1.25, 0.18, "BBB"),
        (-1.15, 0.2, "D"),
        (1.15, 0.1, "A"),
    ],
)
def test_get_stock_rating(roi, uvar, expected):
    """
    Do a single test for Exercise 3: get_stock_rating.
    """
    steps = [f"actual = hw3.get_stock_rating({roi}, {uvar})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.get_stock_rating(roi, uvar)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "rating_1, rating_2, expected",
    [
        ("AAA", "AA", 1),
        ("AAA", "AAA", 0),
        ("D", "C", -1),
        ("BB", "AA", -1),
        ("C", "C", 0),
        ("BBB", "D", 1),
        ("BBB", "BBB", 0),
    ],
)
def test_compare_stock_ratings(rating_1, rating_2, expected):
    """
    Do a single test for Exercise 4: compare_stock_ratings.
    """
    steps = [
        f"actual = hw3.compare_stock_ratings({rating_1}, {rating_2})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.compare_stock_ratings(rating_1, rating_2)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1.0, 2.0, 3.0], 3.0),
        ([1.0, 2.0, 1.0], 1.0),
        ([1.0, 2.0, 1.5], 1.5),
        ([1.0], 1.0),
        ([1.0, 0.0, 1.0], None),
        ([1.0, 1.0, -1.0], None),
        ([-1.0], None),
    ],
)
def test_find_period_return(prices, expected):
    """
    Do a single test for Exercise 5: find_period_return.
    """
    steps = [f"actual = hw3.find_period_return({prices})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.find_period_return(prices)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1.0, 2.0, 3.0], 0.0),
        ([1.0, 2.5, 1.3], 0.24),
        ([1.0, 1.5], 0.0),
        ([1.0], 0.0),
        ([1.0, 0.0, 1.0], None),
        ([1.0, 1.0, -1.0], None),
        ([-1.0], None),
        ([1.0, 2.5, 1.3, 2.5, 2.6], 0.12),
    ],
)
def test_find_avg_var(prices, expected):
    """
    Do a single test for Exercise 6: find_avg_var.
    """
    steps = [f"actual = hw3.find_avg_var({prices})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.find_avg_var(prices)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1.01, 1.06, 1.07, 1.08, 1.13], "AAA"),
        ([1.01, 1.06, 1.07, 1.08, 1.08], "D"),
        ([1.01, 0.06, 1.07, 0.08, 1.13], "D"),
        ([1.01, 1.06, 1.07, 0.08, 1.23], "BB"),
        ([1.01, 0.06, 1.07, 0.08, 1.43], "C"),
        ([1.01, 1.06, 1.07, 1.08, 1.43], "AAA"),
        ([1.01, 1.06, 1.07, 0.38, 1.23], "BBB"),
        ([1.01], "D"),
        ([1.01, 1.06, 1.07, 0.38, 11.23], "BBB"),
        ([1.01, 0.06, 1.07, 0.38, 11.23], "C"),
        ([1.01, 0.06, 1.07, -0.38, 11.23], None),
        ([1.01, 1.16, 1.00, 0.88, 1.23], "AA"),
        ([1.01, 1.16, 1.00, 0.68, 1.23], "A"),
    ],
)
def test_find_stock_rating_from_prices(prices, expected):
    """
    Do a single test for Exercise 7: find_stock_rating_from_prices.
    """
    steps = [
        f"actual = hw3.find_stock_rating_from_prices({prices})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.find_stock_rating_from_prices(prices)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
