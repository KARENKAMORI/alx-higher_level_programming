#!/usr/bin/python3
"""Module: Rectangle.

Contains a Rectangle class that inherits from
BaseGeometry and other methods.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Checks and sets the Rectangle class default attributes."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Sets str behaviour."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height
