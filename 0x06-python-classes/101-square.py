#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square representation."""

    def __init__(self, size=0, position=(0, 0)):
        """New square initialization.

        Args:
            size (int): The new square size.
            position (int, int): The new square position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the square's current position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the # character in square."""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for y in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() Square representation."""
        if self.__size != 0:
            [print("") for x in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
