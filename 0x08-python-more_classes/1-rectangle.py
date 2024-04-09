#!/usr/bin/python3
"""Module: Rectangle.

This module contains a rectangle defining class.

"""


class Rectangle():
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Sets the necessary Rectangle object attributes.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get or set the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
