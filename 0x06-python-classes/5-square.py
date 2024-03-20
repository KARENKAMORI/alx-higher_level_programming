#!/usr/bin/python3
""" class Square defining a square"""


class Square:
    """ class Square defining a square"""
    def __init__(self, size=0):
        """ dander init square

        Args:
            value (int): square size.
        """
        self.size = size

    @property
    def size(self):
        """int: size - private.

        Returns:
            size - private.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size value, must be int.

        Args:
            value (int): square size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """returns square's area

        Returns:
            square area.
        """
        return self.__size**2

    def my_print(self):
        """printing square with the character # in stdout"""

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
