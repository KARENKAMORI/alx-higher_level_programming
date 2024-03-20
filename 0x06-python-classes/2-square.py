#!/usr/bin/python3
""" class Square defining a square"""


class Square:
    """ class Square defining a square"""

    def __init__(self, size=0):
        """square initialization
        Args:
            size (int): square size.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  # square size
