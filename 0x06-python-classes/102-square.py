#!/usr/bin/python3
""" class Square defining a square"""


class Square:
    """ class Square defining a square"""
    def __init__(self, size=0):
        """ dander init square method

        Args:
            value (int): square size.
        """
        self.size = size

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size value, must be int.

        Args:
            value (int): square size.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: square size.

    def area(self):
        """returns the calculated area

        Returns:
            calculated area.
        """
        return self.__size**2

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size
