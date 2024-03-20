#!/usr/bin/python3
""" class Square defining a square"""


class Square:
    """ class Square defining square"""

    def __init__(self, size=0):
        """square initialization
        Args:
            size (int): square size
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: square size

    def area(self):
        """returns square area.

        Returns:
            area.
        """
        return self.__size**2
