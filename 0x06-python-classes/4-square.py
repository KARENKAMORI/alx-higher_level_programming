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
        """Sets size value, must be an integer.

        Args:
            value (int): square size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: square size

    def area(self):
        """returns square area

        Returns:
            area.
        """
        return self.__size**2
