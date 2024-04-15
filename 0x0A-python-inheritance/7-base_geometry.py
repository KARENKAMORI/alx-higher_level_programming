#!/usr/bin/python3
"""Module: BaseGeometry.

Contains an empty BaseGeometry class.
"""


class BaseGeometry():
    """The BaseGeometry defining class."""

    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validation."""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
