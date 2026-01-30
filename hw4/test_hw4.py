"""
CMSC 14100 - Winter 2026

Test code for Homework 4
"""

import hw4
import json
import os

import sys
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw4"

@pytest.mark.parametrize("password, expected",
                            [
                                ("", [0, 0, 0]),
                                ("a", [1, 0, 0]),
                                ("xyz", [3, 0, 0]),
                                ("xyz123", [3, 3, 0]),
                                ("x1y2z3", [3, 3, 0]),
                                ("!x1y2z3", [3, 3, 1]),
                                ("!!!x1y2z3", [3, 3, 3]),
                                ("x1!y2!z3!", [3, 3, 3])
                            ])
def test_count_number_of_each(password, expected):
    steps = [f"actual = hw4.count_number_of_each('{password}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.count_number_of_each(password)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("input, password, wildcards, expected",
                            [
                                ("abc", "abc", [], -1),
                                ("abc", "abc", ["*"], -1),
                                ("abc", "a*c", ["*"], -1),
                                ("abc", "***", ["*"], -1),
                                ("abc", "***", ["&", "*", "!"], -1),
                                ("Password", "pa**word", ["&", "*", "!"], 0),
                                ("password", "pasSword", ["&", "*", "!"], 3),
                                ("passward", "pa**word", ["&", "*", "!"], 5),
                                ("Password", "!a**word", ["&", "*", "!"], -1),
                                ("sword", "p%ssw%rd", ["%", "!"], 0),
                                ("pass", "p%ssw%rd", ["%", "!"], 4), 
                                ("password", "p%ss", ["%", "!"], 4)
                            ])
def test_compare(input, password, wildcards, expected):
    steps = [f"actual = hw4.compare('{input}', '{password}', {wildcards})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.compare(input, password, wildcards)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("password, expected",
                            [
                                ("abc", 0),
                                ("abcDe", 1),
                                ("abc123", 6),
                                ("a1b2c3", 6),
                                ("AbCdE", 3),
                                ("abc&123", 8),
                                ("abc123!!", 10),
                                ("aaaaaaaaa", 3),
                                ("abc!123!!", 15)
                            ])
def test_compute_strength(password, expected):
    steps = [f"actual = hw4.compute_strength('{password}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.compute_strength(password)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("length, password, expected",
                            [
                                (1, "a", 1),
                                (1, "b", 2),
                                (1, "x", 24),
                                (2, "aa", 1),
                                (2, "ax", 24),
                                (2, "bx", 50),
                                (2, "cx", 76),
                                (3, "aab", 2)
                            ])
def test_brute_force_attack(length, password, expected):
    steps = [f"actual = hw4.brute_force_attack({length}, '{password}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.brute_force_attack(length, password)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("phrase, strength, expected",
                            [
                                ("Hello, world", 0, "Hw"),
                                ("Hello, world", 1, "Hw"),
                                ("Hello, world", 2, "Hw!"),
                                ("Hello, world", 4, "Hw!!"),
                                ("Hi how are you today?", 0, "Hhayt"),
                                ("Hi how are U today?", 2, "HhaUt"),
                                ("Hi how are U today?", 3, "HhaUt!"),
                                ("Hi how are U today?", 8, "HhaUt!!!"),
                                ("Hi how are U 2day?", 8, "HhaU2!!"),
                            ])
def test_create_password(phrase, strength, expected):
    steps = [f"actual = hw4.create_password('{phrase}', {strength})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.create_password(phrase, strength)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
