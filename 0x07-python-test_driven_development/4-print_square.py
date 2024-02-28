#!/usr/bin/python3
"""Function prints square."""

def print_square(size):
    """Prints square with #.
    Args:
        size: Height and width of square.
    Raise:
        TypeError: If not int.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("x" * size)
