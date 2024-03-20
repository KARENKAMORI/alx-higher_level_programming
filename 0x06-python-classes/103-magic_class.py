#!/usr/bin/python3
"""Defining a MagicClass exactly matching the provided Holberton bytecode."""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """MagicClass initialization.

        Arg:
            radius (float or int): The new MagicClass radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the MagicClass area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the MagicClass circumfrence."""
        return (2 * math.pi * self.__radius)
