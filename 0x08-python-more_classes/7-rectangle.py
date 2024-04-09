#!/usr/bin/python3
"""Module: Rectangle.

This module contains a rectangle class definition.

"""


class Rectangle():
    """Rectangle definition."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Sets the necessary Rectangle object attributes.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Sets the Rectangle object print behavior."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """Sets the Rectangle object repr behavior."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

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

    def area(self):
        """Returns the area of the current rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the current rectangle."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __del__(self):
        """Sets the Rectangle object del behavior."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
