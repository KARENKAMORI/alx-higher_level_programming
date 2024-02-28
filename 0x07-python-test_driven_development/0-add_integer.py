#!/usr/bin/python3
"""Integer addition function."""

def add_integer(a, b=98):
    """Return value: a + b.
    floats are casted into integers before addition.
    Raises:
        TypeError: if a or b is not a float or an int.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
