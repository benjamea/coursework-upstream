"""
CMSC 14100
Winter 2026

Test code for Homework #8
"""

import os
import sys
import random

import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw8  # noqa: E402
import helpers  # noqa: E402

MODULE = "hw8"
POINTS = [
    hw8.Point2D(0, 0),
    hw8.Point2D(1, 1),
    hw8.Point2D(2, 0),
    hw8.Point2D(0, 2),
    hw8.Point2D(2, 2),
]
BOXES = [hw8.Box2D(0, 1, 0, 1), hw8.Box2D(0, 2, 0, 2), hw8.Box2D(-1, 2, -1, 2)]

NODE_VALID_1 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_VALID_1_REPR = """
Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=0
"""
NODE_VALID_2 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_VALID_2.points = [hw8.Point2D(0.5, 0.5)]
NODE_VALID_2_REPR = """
Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=1
"""
NODE_VALID_3 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_VALID_3.points = [hw8.Point2D(1, 1)]
NODE_VALID_3_REPR = """
Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=1
"""
NODE_INVALID_1 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_INVALID_1.children = [NODE_VALID_1]
NODE_INVALID_1.points = [hw8.Point2D(1, 1)]
NODE_INVALID_1_REPR = """
Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=1
    Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=0
"""
NODE_INVALID_2 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_INVALID_2.children = [NODE_VALID_1, NODE_VALID_2]
NODE_INVALID_2.points = [hw8.Point2D(1, 1)]
NODE_INVALID_2_REPR = """
Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=1
    Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=0
    Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=1
"""

NODE_INVALID_3 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_INVALID_3.children = [NODE_VALID_1, NODE_INVALID_1]
NODE_INVALID_3_REPR = """
Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=0
    Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=0
    Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=1
        Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=0
"""

NODE_VALID_1_REPR0 = """Box2D(min_x=0, max_x=1, min_y=0, max_y=1) with Points=0"""
NODE_VALID_1_REPR1 = """Box2D(min_x=0, max_x=1, min_y=0, max_y=1)
    Box2D(min_x=0, max_x=0.5, min_y=0, max_y=1) with Points=0
    Box2D(min_x=0.5, max_x=1, min_y=0, max_y=1) with Points=0"""

NODE_VALID_1_REPR2 = """Box2D(min_x=0, max_x=1, min_y=0, max_y=1)
    Box2D(min_x=0, max_x=0.5, min_y=0, max_y=1)
        Box2D(min_x=0, max_x=0.5, min_y=0, max_y=0.25) with Points=0
        Box2D(min_x=0, max_x=0.5, min_y=0.25, max_y=1) with Points=0
    Box2D(min_x=0.5, max_x=1, min_y=0, max_y=1)
        Box2D(min_x=0.5, max_x=1, min_y=0, max_y=0.75) with Points=0
        Box2D(min_x=0.5, max_x=1, min_y=0.75, max_y=1) with Points=0"""

NODE_VALID_1_REPR3 = """Box2D(min_x=0, max_x=1, min_y=0, max_y=1)
    Box2D(min_x=0, max_x=0.5, min_y=0, max_y=1)
        Box2D(min_x=0, max_x=0.5, min_y=0, max_y=0.25)
            Box2D(min_x=0, max_x=0.25, min_y=0, max_y=0.25) with Points=0
            Box2D(min_x=0.25, max_x=0.5, min_y=0, max_y=0.25) with Points=0
        Box2D(min_x=0, max_x=0.5, min_y=0.25, max_y=1)
            Box2D(min_x=0, max_x=0.25, min_y=0.25, max_y=1) with Points=0
            Box2D(min_x=0.25, max_x=0.5, min_y=0.25, max_y=1) with Points=0
    Box2D(min_x=0.5, max_x=1, min_y=0, max_y=1)
        Box2D(min_x=0.5, max_x=1, min_y=0, max_y=0.75)
            Box2D(min_x=0.5, max_x=0.75, min_y=0, max_y=0.75) with Points=0
            Box2D(min_x=0.75, max_x=1, min_y=0, max_y=0.75) with Points=0
        Box2D(min_x=0.5, max_x=1, min_y=0.75, max_y=1)
            Box2D(min_x=0.5, max_x=0.75, min_y=0.75, max_y=1) with Points=0
            Box2D(min_x=0.75, max_x=1, min_y=0.75, max_y=1) with Points=0"""

NODE_BUILD_0 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_BUILD_1 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_BUILD_1.children = [hw8.Space2DNode(hw8.Box2D(0, 0.5, 0, 1)), hw8.Space2DNode(hw8.Box2D(0.5, 1, 0, 1))]
NODE_BUILD_2 = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
NODE_BUILD_2.children = [hw8.Space2DNode(hw8.Box2D(0, 0.5, 0, 1)), hw8.Space2DNode(hw8.Box2D(0.5, 1, 0, 1))]
NODE_BUILD_2.children[0].children = [hw8.Space2DNode(hw8.Box2D(0, 0.5, 0, 0.5)), hw8.Space2DNode(hw8.Box2D(0, 0.5, 0.5, 1))]
NODE_BUILD_2.children[1].children = [hw8.Space2DNode(hw8.Box2D(0.5, 1, 0, 0.5)), hw8.Space2DNode(hw8.Box2D(0.5, 1, 0.5, 1))]

@pytest.mark.parametrize(
    "box, dim",
    [
        (BOXES[0], 0),
        (BOXES[1], 1),
        (BOXES[2], 0),
    ],
)
def test_split_box_on_dimension(box, dim):
    steps = [f"actual = hw8.split_box_on_dimension({box}, {dim})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.split_box_on_dimension(box, dim)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    assert len(actual) == 2, "The split did not return exactly 2 boxes"

    assert box not in actual, "Duplicate reference to the original box found"

    min_x = min(actual[0].min_x, actual[1].min_x)
    min_y = min(actual[0].min_y, actual[1].min_y)
    max_x = max(actual[0].max_x, actual[1].max_x)
    max_y = max(actual[0].max_x, actual[1].max_y)

    expected_box_dims = (box.min_x, box.min_y, box.max_x, box.max_y)
    actual_box_dims = (min_x, min_y, max_x, max_y)

    assert (
        expected_box_dims == actual_box_dims
    ), "The split boxes do not cover the original box"

    if dim == 0:
        assert actual[0].max_y == box.max_y, "Y coordinate changed while splitting on x"
    else:
        assert actual[0].max_x == box.max_x, "X coordinate changed while splitting on y"


@pytest.mark.parametrize(
    "node, expected",
    [
        (NODE_VALID_1, True),
        (NODE_VALID_2, True),
        (NODE_VALID_3, True),
        (NODE_INVALID_1, False),
        (NODE_INVALID_2, False),
        (NODE_INVALID_3, False),
    ],
)
def test_is_valid_node(node, expected):
    steps = [f"actual = node.is_valid_node()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = node.is_valid_node()
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "var_name, node, expected",
    [
        ("NODE_VALID_1", NODE_VALID_1, NODE_VALID_1_REPR),
        ("NODE_VALID_2", NODE_VALID_2, NODE_VALID_2_REPR),
        ("NODE_VALID_3", NODE_VALID_3, NODE_VALID_3_REPR),
        ("NODE_INVALID_1", NODE_INVALID_1, NODE_INVALID_1_REPR),
        ("NODE_INVALID_2", NODE_INVALID_2, NODE_INVALID_2_REPR),
        ("NODE_INVALID_3", NODE_INVALID_3, NODE_INVALID_3_REPR),
    ],
)
def test_repr_node(var_name, node, expected):
    steps = [f"import test_hw8.py; test_hw8.{var_name}"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = node.__repr__().replace("\t", " " * 4)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual.strip(), expected.strip())
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "depth, expected",
    [
        (0, NODE_BUILD_0),
        (1, NODE_BUILD_1),
        (2, NODE_BUILD_2),
    ],
)
def test_build(depth, expected):
    steps = [f"node = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1)); node.build({depth})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        node = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
        node.build(depth)
        actual = node
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual.__repr__(), expected.__repr__())
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


def test_insert_correct_points():
    # First test, add random point, is it correct?
    tree = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
    p = hw8.Point2D(random.random(), random.random())
    tree.insert(p)

    p = hw8.Point2D(random.random(), random.random())
    tree.insert(p)
    assert tree.is_valid_node(), "The tree is not valid after insertion"

    assert len(tree.points) == 2, "Unexpected number of points in the tree"


def test_insert_boundaries():
    # Are boundary points handled properly?
    tree = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
    child1 = hw8.Space2DNode(hw8.Box2D(0, 0.5, 0, 1))
    child2 = hw8.Space2DNode(hw8.Box2D(0.5, 1, 0, 1))
    tree.children = [child1, child2]

    p = hw8.Point2D(0.5, 0.5)
    tree.insert(p)

    assert tree.is_valid_node(), "The tree is not valid after insertion"

    assert (
        len(child1.points) == 1 and len(child2.points) == 0
    ), "Unexpected number of points in the tree"


def test_insert_random():
    # Random insertions, is valid for all
    tree = hw8.Space2DNode(hw8.Box2D(0, 1, 0, 1))
    tree.build(4)

    # add 100 random points and ensure validity
    for i in range(100):

        p = hw8.Point2D(random.random(), random.random())

        tree.insert(p)

        assert tree.is_valid_node(), f"Insertion {i} results in an invalid tree"


def _get_closest_point(points, query):
    """
    Return the closest point in a list to a query point.

    Args:
        points (list[Point2D]): Points to search.
        query (Point2D): Query point.

    Returns:
        Point2D or None:
            Closest point in the list, or None if empty.
    """
    if len(points) == 0:
        return None

    # sort by distances, get closest
    lst = [(p.distance_to(query), p) for p in points]
    lst.sort()

    return lst[0][1]


def test_get_nearest_neighbor_one_point():
    # create a kd tree with depth 4
    tree = hw8.Tree(0, 1, 0, 1, 2)
    p1 = hw8.Point2D(0.1, 0.1)
    tree.insert(p1)

    p2 = hw8.Point2D(0.5, 0.5)
    assert p1 == tree.get_nearest_neighbor(p2), "Nearest neighbor not found"


def test_get_nearest_neighbor_two_points():
    # create a kd tree with depth 4
    tree = hw8.Tree(0, 1, 0, 1, 2)
    p1 = hw8.Point2D(0.1, 0.1)
    p2 = hw8.Point2D(0.4, 0.4)
    tree.insert(p1)
    tree.insert(p2)

    p3 = hw8.Point2D(0.5, 0.5)
    assert p2 == tree.get_nearest_neighbor(p3), "Correct nearest neighbor not found"


def test_get_nearest_neighbor_boundary():
    # create a kd tree with depth 4
    tree = hw8.Tree(0, 1, 0, 1, 2)
    p1 = hw8.Point2D(0.1, 0.1)
    p2 = hw8.Point2D(0.5, 0.5)
    tree.insert(p1)
    tree.insert(p2)

    p3 = hw8.Point2D(0.5, 0.5)
    assert p2 == tree.get_nearest_neighbor(p3), "Correct nearest neighbor not found"


def test_get_nearest_neighbor_random():
    # create a kd tree with depth 4
    tree = hw8.Tree(0, 1, 0, 1, 4)

    # add 100 random points to the tree.
    point_lst = []
    for i in range(100):

        p = hw8.Point2D(random.random(), random.random())

        point_lst.append(p)

        tree.insert(p)

        assert tree.root.is_valid_node(), f"Insertion {i} results in an invalid tree"

    # try a 100 random queries.
    for i in range(100):

        p = hw8.Point2D(random.random(), random.random())

        expected = _get_closest_point(point_lst, p)
        actual = tree.get_nearest_neighbor(p)

        assert (
            expected == actual
        ), f"Query {i} results in an incorrect result {actual} != {expected}"
