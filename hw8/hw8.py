"""
CMSC 14100
Winter 2026
Homework #8

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math
import copy

X, Y = 0, 1


class Point2D:
    """
    Represents a point in 2-dimensional Cartesian space.

    A Point2D object stores x and y coordinates as floating-point values
    and provides helper methods for computing distances.

    This class is useful for geometric data structures.
    """

    def __init__(self, x, y):
        """
        Initialize a new 2D point.

        Args:
            x (int or float): The x-coordinate.
            y (int or float): The y-coordinate.
        """
        self.x = float(x)
        self.y = float(y)

    def distance_squared_to(self, other):
        """
        Compute the squared Euclidean distance to another point.

        We often compute squared distance because it avoids the expensive
        square root operation.

        Args:
            other (Point2D): Another point.

        Returns:
            float: Squared distance between the two points.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return dx * dx + dy * dy

    def distance_to(self, other):
        """
        Compute the Euclidean distance to another point.

        Args:
            other (Point2D): Another point.

        Returns:
            float: Distance between the two points.
        """
        return math.sqrt(self.distance_squared_to(other))

    def get(self, dim):
        """
        Return coordinate value by dimension index.

        Args:
            dim (int): 0 for x-coordinate, 1 for y-coordinate.

        Returns:
            float: The requested coordinate value.

        Raises:
            ValueError: If dim is not 0 or 1.
        """
        if dim == 0:
            return self.x
        elif dim == 1:
            return self.y
        else:
            raise ValueError("Dimension must be 0 (x) or 1 (y).")

    def distance_to_segment(self, p1, p2):
        """
        Compute the shortest distance from this point to a line segment.

        The segment is defined by endpoints p1 and p2.

        This works by:
        1. Projecting this point onto the infinite line.
        2. Clamping that projection to stay within the segment.
        3. Computing the distance to the closest point.

        Args:
            p1 (Point2D): First endpoint.
            p2 (Point2D): Second endpoint.

        Returns:
            float: Minimum distance to the segment.
        """

        # Vector from p1 to this point
        vx = self.x - p1.x
        vy = self.y - p1.y

        # Vector from p1 to p2 (the segment direction)
        sx = p2.x - p1.x
        sy = p2.y - p1.y

        segment_length_squared = sx * sx + sy * sy

        # Handle degenerate segment (p1 == p2)
        if segment_length_squared == 0:
            return self.distance_to(p1)

        # Project this point onto the infinite line defined by p1->p2
        # Compute projection factor t
        t = (vx * sx + vy * sy) / segment_length_squared

        # Clamp t to [0, 1] so that projection lies on the segment
        t = max(0.0, min(1.0, t))

        # Compute closest point on the segment
        closest_x = p1.x + t * sx
        closest_y = p1.y + t * sy
        closest_point = Point2D(closest_x, closest_y)

        return self.distance_to(closest_point)

    def __repr__(self):
        """Return string representation."""
        return f"Point2D(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """Check coordinate equality."""
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y


class Box2D:
    """
    Represents an axis-aligned bounding box in 2D space.

    The box is defined by:
        min_x, max_x, min_y, max_y

    The box edges are parallel to the coordinate axes.
    """

    def __init__(self, min_x, max_x, min_y, max_y):
        """
        Initialize a bounding box.

        Args:
            min_x (float): Minimum x value.
            max_x (float): Maximum x value.
            min_y (float): Minimum y value.
            max_y (float): Maximum y value.
        """
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def distance_to_point(self, point):
        """
        Determine how a point relates to this box.

        Returns:
            -1 if the point is strictly inside the box.
             0 if the point lies on the boundary.
             d (float) if outside, where d is the distance to the box.
        """

        # Check if inside or on boundary
        inside_x = self.min_x < point.x < self.max_x
        inside_y = self.min_y < point.y < self.max_y

        on_boundary = (
            (point.x == self.min_x or point.x == self.max_x)
            and self.min_y <= point.y <= self.max_y
        ) or (
            (point.y == self.min_y or point.y == self.max_y)
            and self.min_x <= point.x <= self.max_x
        )

        if inside_x and inside_y:
            return -1

        if on_boundary:
            return 0

        # If outside, compute distance to nearest point on the box.
        # Clamp the point to the box to find the closest point.
        clamped_x = min(max(point.x, self.min_x), self.max_x)
        clamped_y = min(max(point.y, self.min_y), self.max_y)

        closest_point = Point2D(clamped_x, clamped_y)

        return point.distance_to(closest_point)

    def __repr__(self):
        """
        String representation for debugging.
        """
        return (
            f"Box2D(min_x={self.min_x}, max_x={self.max_x}, "
            f"min_y={self.min_y}, max_y={self.max_y})"
        )


def split_box_on_dimension(box, dim):
    """TODO"""
    raise ValueError("Not Implemented")


class Space2DNode:
    """
    A single spatial node.

    Each node represents a rectangular region (Box2D) and may either:
        - Store points (leaf node), OR
        - Have two children (internal node)
    """

    def __init__(self, box):
        """
        Initialize a Space2DNode.

        Args:
            box (Box2D): The spatial region represented by this node.
        """
        self.box = box
        self.children = []
        self.points = []

    def is_valid_node(self):
        """TODO"""
        raise ValueError("Not Implemented")

    def build(self, depth):
        """TODO"""
        raise ValueError("Not Implemented")

    def insert(self, point):
        """TODO"""
        raise ValueError("Not Implemented")

    def get_nearest_neighbor(self, point):
        """TODO"""
        raise ValueError("Not Implemented")


    def __repr__(self):
        """TODO"""
        raise ValueError("Not Implemented")


class Tree:
    """
    Tree data structure for organizing 2D points.
    """

    def __init__(self, min_x, max_x, min_y, max_y, depth):
        """
        Initialize a Tree.

        Args:
            min_x (float): Minimum x boundary.
            max_x (float): Maximum x boundary.
            min_y (float): Minimum y boundary.
            max_y (float): Maximum y boundary.
            depth (int): Number of subdivision levels.
        """

        assert depth >= 0

        self.root = Space2DNode(Box2D(min_x, max_x, min_y, max_y))

        self.root.build(depth)

    def insert(self, point):
        """Inserts a point into the tree.

        Args:
           point (Point2D): point to insert

        """
        self.root.insert(point)

    def get_nearest_neighbor(self, point):
        """
        Find the closest point in the tree to a query point.

        This is the public method students should call.

        Args:
            point (Point2D): The query point.

        Returns:
            Point2D or None:
                The closest point stored in the tree,
                or None if the tree contains no points.
        """
        return self.root.get_nearest_neighbor(point)

    def __repr__(self):
        """
        String representation for debugging.
        """
        return self.root.__repr__()
