#!/usr/bin/python3
"""Module: Student.

Has a Student class and methods.
"""


class Student():
    """Class defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Sets the Student object necessary attributes.

        Args:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a Student instance dictionary representation."""
        if attrs is not None:
            return {x: y for x, y in self.__dict__.items() if x in attrs}
        return self.__dict__
