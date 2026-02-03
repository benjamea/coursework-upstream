"""
CMSC 14100
Winter 2026

Test code for Homework #5
"""

import copy
import json
import os
import sys
import traceback
import pytest
import helpers as helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw5

MODULE = "hw5"


def comparison_helper(matrix):
    """
    Takes a list of lists of floats and returns a new list of lists where:
      - Each float is rounded to the nearest 2nd decimal place.
      - Each value is formatted as a string with 2 decimal places.

    Args:
        matrix (list of list of float): The input 2D list of floats.

    Returns:
        list of list of str: A new 2D list where each float is rounded and formatted as a string.
    """

    # basically creates interpretable floating point failures that bubble up through pytest...
    try:
        return [[f"{round(value, 2):.2f}" for value in row] for row in matrix]
    except:
        return str(matrix)


# 1. Small 2x2 image
IMAGE_2x2 = [[0.0, 0.5], [1.0, 0.2]]
IMAGE_2x2_PRINT = " +\n# \n"

IMAGE_2x2b = [[1.0, 0.5], [0.0, 0.8]]
IMAGE_2x2b_PRINT = "#+\n #\n"

IMAGE_2x2c = [[0.0, 0.0], [0.0, 0.0]]
IMAGE_2x2c_PRINT = "  \n  \n"

# 2. 3x2 image (rectangular)
IMAGE_3x2 = [[0.1, 0.4, 0.9], [0.7, 0.3, 0.2]]

# 3. 2x3 image with a gradient
IMAGE_2x3 = [[0.0, 0.5, 1.0], [0.2, 0.6, 0.8]]

# 4. 1x4 single-row image
IMAGE_1x4 = [[0.1, 0.2, 0.3, 0.4]]
IMAGE_1x4_PRINT = "  --\n"

# 5. 4x1 single-column image
IMAGE_4x1 = [[0.0], [0.25], [0.5], [0.75]]
IMAGE_4x1_PRINT = " \n-\n+\n#\n"

# 1. Checkerboard pattern (alternating 0.0 and 1.0)
IMAGE_9x9_CHECKER = [
    [0.0 if (i + j) % 2 == 0 else 1.0 for j in range(9)] for i in range(9)
]

# 2. Horizontal gradient (0.0 to 1.0 across columns)
IMAGE_9x9_HGRAD = [[j / 8 for j in range(9)] for i in range(9)]

# 3. Vertical gradient (0.0 to 1.0 across rows)
IMAGE_9x9_VGRAD = [[i / 8 for j in range(9)] for i in range(9)]

# 4. Diagonal gradient (0.0 at top-left to 1.0 at bottom-right)
IMAGE_9x9_DIAG = [[(i + j) / 16 for j in range(9)] for i in range(9)]

# 5. Cross pattern (1.0 in center row/column, 0.0 elsewhere)
IMAGE_9x9_CROSS = [
    [1.0 if i == 4 or j == 4 else 0.0 for j in range(9)] for i in range(9)
]


@pytest.mark.parametrize(
    "image1, image2, alpha, expected",
    [
        (IMAGE_2x2, IMAGE_2x2b, 0.5, [[0.5, 0.5], [0.5, 0.5]]),
        (IMAGE_2x2, IMAGE_2x2c, 0.75, [[0.0, 0.375], [0.75, 0.15]]),
        (IMAGE_2x2b, IMAGE_2x2c, 1, [[1.0, 0.5], [0.0, 0.8]]),
        (IMAGE_2x2c, IMAGE_2x2b, 0, [[1.0, 0.5], [0.0, 0.8]]),
    ],
)
def test_alpha_composite(image1, image2, alpha, expected):
    """
    Test code for alpha_composite
    """
    steps = [
        f"image1 = {image1}",
        f"image2 = {image2}",
        f"actual = hw5.alpha_composite(image1, image2, {alpha})",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    copy1 = copy.deepcopy(image1)  # check that the image is unmodified
    copy2 = copy.deepcopy(image2)  # check that the image is unmodified

    try:
        actual = hw5.alpha_composite(image1, image2, alpha)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(
        comparison_helper(actual), comparison_helper(expected)
    )
    if err_msg is not None:
        actual_formatted = f"\t## returns {actual} instead of {expected}"
        pytest.fail(err_msg + recreate_msg + actual_formatted)

    err_msg = helpers.check_2D_list_unmodified("image1", image1, copy1)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_2D_list_unmodified("image2", image2, copy2)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "image, crop_params, expected",
    [
        (IMAGE_2x2, [0, 1, 1, 1], [[0.5]]),
        (IMAGE_2x2b, [1, 1, 1, 1], [[0.8]]),
        (IMAGE_9x9_CHECKER, [6, 7, 2, 2], [[1.0, 0.0], [0.0, 1.0]]),
        (IMAGE_1x4, [0, 0, 1, 4], [[0.1, 0.2, 0.3, 0.4]]),
        (IMAGE_2x2, [0, 0, 2, 2], [[0.0, 0.5], [1.0, 0.2]]),
        (IMAGE_2x2, [0, 0, 3, 3], None),
    ],
)
def test_crop(image, crop_params, expected):
    """
    Test code for crop
    """
    formatted_params = ",".join([str(param) for param in crop_params])
    steps = [f"image = {image}", f"actual = hw5.crop(image, {formatted_params})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    copy1 = copy.deepcopy(image)  # check that the image is unmodified

    try:
        actual = hw5.crop(image, *crop_params)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        actual_formatted = f"\t## returns {actual} instead of {expected}"
        pytest.fail(err_msg + recreate_msg + actual_formatted)

    err_msg = helpers.check_2D_list_unmodified("image", image, copy1)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "image, pixel, expected",
    [
        (IMAGE_9x9_CHECKER, [4, 5], 1.0),
        (IMAGE_9x9_HGRAD, [7, 7], 0.875),
        (IMAGE_9x9_VGRAD, [5, 3], 0.625),
        (IMAGE_9x9_DIAG, [5, 4], 0.5625),
        (IMAGE_9x9_CROSS, [3, 6], 0.0),
        (IMAGE_2x2, [0, 0], 0.0),
        (IMAGE_1x4, [0, 0], 0.1),
    ],
)
def test_median_blur(image, pixel, expected):
    """
    Test code for median_blur
    """
    steps = [
        f"image = {image}",
        f"actual = hw5.median_blur(image)[{pixel[0]}][{pixel[1]}]",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    copy1 = copy.deepcopy(image)  # check that the image is unmodified

    try:
        actual = hw5.median_blur(image)[pixel[0]][pixel[1]]
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(
        comparison_helper(actual), comparison_helper(expected)
    )
    if err_msg is not None:
        actual_formatted = f"\t## returns {actual} instead of {expected}"
        pytest.fail(err_msg + recreate_msg + actual_formatted)

    err_msg = helpers.check_2D_list_unmodified("image", image, copy1)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "image, pixel, k, expected",
    [
        (IMAGE_9x9_CHECKER, [31, 16], 7, 0.0),
        (IMAGE_9x9_HGRAD, [20, 20], 3, 0.75),
        (IMAGE_9x9_VGRAD, [5, 3], 2, 0.25),
        (IMAGE_9x9_DIAG, [16, 0], 2, 0.5),
        (IMAGE_9x9_CROSS, [21, 17], 4, 1.0),
        (IMAGE_2x2, [3, 3], 2, 0.2),
        (IMAGE_1x4, [12, 13], 15, 0.1),
    ],
)
def test_resize_up(image, pixel, k, expected):
    """
    Test code for resize_up
    """
    steps = [
        f"image = {image}",
        f"actual = hw5.resize_up(image, {k})[{pixel[0]}][{pixel[1]}]",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    copy1 = copy.deepcopy(image)  # check that the image is unmodified

    try:
        actual = hw5.resize_up(image, k)[pixel[0]][pixel[1]]
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(
        comparison_helper(actual), comparison_helper(expected)
    )
    if err_msg is not None:
        actual_formatted = f"\t## returns {actual} instead of {expected}"
        pytest.fail(err_msg + recreate_msg + actual_formatted)

    err_msg = helpers.check_2D_list_unmodified("image", image, copy1)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "image, pixel, kh, kv, expected",
    [
        (IMAGE_9x9_CHECKER, [11, 16], 7, 3, 1.0),
        (IMAGE_9x9_HGRAD, [20, 20], 3, 3, 0.25),
        (IMAGE_9x9_VGRAD, [5, 3], 2, 1, 0.625),
        (IMAGE_9x9_DIAG, [16, 0], 2, 14, 0.4375),
        (IMAGE_9x9_CROSS, [21, 17], 4, 4, 0.0),
        (IMAGE_2x2, [3, 3], 2, 2, 0.2),
        (IMAGE_1x4, [12, 13], 15, 15, 0.2),
    ],
)
def test_tile_image(image, pixel, kh, kv, expected):
    """
    Test code for tile_image
    """
    steps = [
        f"image = {image}",
        f"actual = hw5.tile_image(image, {kh}, {kv})[{pixel[0]}][{pixel[1]}]",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    copy1 = copy.deepcopy(image)  # check that the image is unmodified

    try:
        actual_image = hw5.tile_image(image, kh, kv)
        actual = actual_image[pixel[0]][pixel[1]]
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(
        comparison_helper(actual), comparison_helper(expected)
    )
    if err_msg is not None:
        actual_formatted = f"\t## returns {actual} instead of {expected}"
        pytest.fail(err_msg + recreate_msg + actual_formatted)

    err_msg = helpers.check_2D_list_unmodified("image", image, copy1)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # check tiling dimensions
    h = len(image)
    w = len(image[0])

    ha = len(actual_image)
    wa = len(actual_image[0])

    if h * kv != ha or w * kh != wa:
        err_msg = (
            f"\t # Expected final dimensions {w * kh} x {h * kv}, but got {wa} x {ha}"
        )
        pytest.fail(recreate_msg + err_msg)


@pytest.mark.parametrize(
    "image, pixel, k, expected",
    [
        (IMAGE_9x9_CHECKER, [31, 16], 7, 0.0),
        (IMAGE_9x9_HGRAD, [20, 20], 3, 0.75),
        (IMAGE_9x9_VGRAD, [5, 3], 2, 0.25),
        (IMAGE_9x9_DIAG, [16, 0], 2, 0.5),
        (IMAGE_9x9_CROSS, [21, 17], 4, 1.0),
        (IMAGE_2x2, [3, 3], 2, 0.2),
        (IMAGE_1x4, [12, 13], 15, 0.1),
    ],
)
def test_resize_up(image, pixel, k, expected):
    """
    Test code for resize_up
    """
    steps = [
        f"image = {image}",
        f"actual = hw5.resize_up(image, {k})[{pixel[0]}][{pixel[1]}]",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    copy1 = copy.deepcopy(image)  # check that the image is unmodified

    try:
        actual = hw5.resize_up(image, k)[pixel[0]][pixel[1]]
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(
        comparison_helper(actual), comparison_helper(expected)
    )
    if err_msg is not None:
        actual_formatted = f"\t## returns {actual} instead of {expected}"
        pytest.fail(err_msg + recreate_msg + actual_formatted)

    err_msg = helpers.check_2D_list_unmodified("image", image, copy1)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "image, expected",
    [
        (IMAGE_2x2, IMAGE_2x2_PRINT),
        (IMAGE_2x2b, IMAGE_2x2b_PRINT),
        (IMAGE_2x2c, IMAGE_2x2c_PRINT),
        (IMAGE_1x4, IMAGE_1x4_PRINT),
        (IMAGE_4x1, IMAGE_4x1_PRINT),
    ],
)
def test_pretty_print(image, expected, capsys):
    """
    Test code for pretty_print
    """
    steps = [
        f"image = {image}",
        f"actual = hw5.pretty_print(image)",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        hw5.pretty_print(image)
        actual = capsys.readouterr().out
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(
        comparison_helper(actual), comparison_helper(expected)
    )
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
