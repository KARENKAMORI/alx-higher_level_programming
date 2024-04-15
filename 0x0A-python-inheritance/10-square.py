#!/usr/bin/python3
"""Module: Square.

Contains a Rectangle inheriting class Square
and other methods.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Checks and sets the Square class default attributes."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
