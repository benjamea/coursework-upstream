"""
CMSC 14100
Win 2026
Homework #5

We will be using anonymous grading, so please do NOT include your name anywhere
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.

What can I use?
    You may NOT import and use any outside libraries or modules.
"""


def alpha_composite(img1, img2, alpha):
    """
    Blend two grayscale images using alpha compositing.

    Args:
        img1 (list[list[float]]): A grayscale image represented as a
            list of rows, where each inner list has the same length
            and contains floats between 0.0 and 1.0.
        img2 (list[list[float]]): A grayscale image with the same
            dimensions as img1, represented the same way.
        alpha (float): A blending weight between 0 and 1.

    Returns:
        list[list[float]]: A new image of the same size where each
            pixel is alpha * img1[r][c] + (1 - alpha) * img2[r][c].
    """
    num_rows = len(img1)
    num_cols = len(img1[0])
    result = []
    for row in range(num_rows):
        new_row = []
        for col in range(num_cols):
            blended = alpha * img1[row][col] + (1 - alpha) * img2[row][col]
            new_row.append(blended)
        result.append(new_row)
    return result


def crop(img, top, left, height, width):
    """
    Crop a rectangular region from a grayscale image.

    Args:
        img (list[list[float]]): A grayscale image represented as a
            list of rows, where each inner list has the same length
            and contains floats between 0.0 and 1.0.
        top (int): The starting row index of the crop region.
        left (int): The starting column index of the crop region.
        height (int): The number of rows in the crop region.
        width (int): The number of columns in the crop region.

    Returns:
        list[list[float]]: A new cropped image, or None if the crop
            region is invalid (out of bounds, negative dimensions, etc.).
    """
    num_rows = len(img)
    num_cols = len(img[0])

    if top < 0 or left < 0 or height <= 0 or width <= 0:
        return None
    if top + height > num_rows or left + width > num_cols:
        return None

    result = []
    for row in range(top, top + height):
        new_row = []
        for col in range(left, left + width):
            new_row.append(img[row][col])
        result.append(new_row)
    return result


def pixel_to_char(pixel):
    """
    Convert a pixel value to its ASCII character representation.

    Args:
        pixel (float): A brightness value between 0.0 and 1.0.

    Returns:
        str: The character representing the pixel brightness.
    """
    if pixel < 0.25:
        return " "
    elif pixel < 0.5:
        return "-"
    elif pixel < 0.75:
        return "+"
    else:
        return "#"


def pretty_print(image):
    """
    Print a grayscale image as ASCII art.

    Args:
        image (list[list[float]]): A grayscale image represented as a
            list of rows, where each inner list has the same length
            and contains floats between 0.0 and 1.0.
    """
    for row in image:
        line = ""
        for pixel in row:
            line += pixel_to_char(pixel)
        print(line)


def median_blur(image):
    """
    Apply a 3x3 median blur to a grayscale image. Border pixels
    keep their original values; interior pixels get the median of
    the 9 surrounding pixels.

    Args:
        image (list[list[float]]): A grayscale image represented as a
            list of rows, where each inner list has the same length
            and contains floats between 0.0 and 1.0.

    Returns:
        list[list[float]]: A new image of the same size with the
            median blur applied. Border pixels retain their original
            values.
    """
    num_rows = len(image)
    num_cols = len(image[0])
    result = []

    for row in range(num_rows):
        new_row = []
        for col in range(num_cols):
            is_border = (row == 0 or row == num_rows - 1 or
                         col == 0 or col == num_cols - 1)
            if is_border:
                new_row.append(image[row][col])
            else:
                neighbors = []
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        neighbors.append(image[row + dr][col + dc])
                neighbors.sort()
                median = neighbors[4]
                new_row.append(median)
        result.append(new_row)
    return result


def resize_up(image, k):
    """
    Scale up a grayscale image by an integer factor k.

    Args:
        image (list[list[float]]): A grayscale image represented as a
            list of rows, where each inner list has the same length
            and contains floats between 0.0 and 1.0.
        k (int): A positive integer scaling factor.

    Returns:
        list[list[float]]: A new image with height * k rows and
            width * k columns, where each pixel maps back to the
            original using floor division.
    """
    num_rows = len(image)
    num_cols = len(image[0])
    result = []

    for row in range(num_rows * k):
        new_row = []
        for col in range(num_cols * k):
            original_row = row // k
            original_col = col // k
            new_row.append(image[original_row][original_col])
        result.append(new_row)
    return result


def tile_image(image, k_horizontal, k_vertical):
    """
    Tile a grayscale image in a grid pattern.

    Args:
        image (list[list[float]]): A grayscale image represented as a
            list of rows, where each inner list has the same length
            and contains floats between 0.0 and 1.0.
        k_horizontal (int): Number of times to repeat each row
            horizontally (>= 1).
        k_vertical (int): Number of times to repeat the entire set
            of rows vertically (>= 1).

    Returns:
        list[list[float]]: A new tiled image. Must not modify the
            original image.
    """
    result = []
    for _ in range(k_vertical):
        for row in image:
            new_row = row * k_horizontal
            result.append(new_row)
    return result