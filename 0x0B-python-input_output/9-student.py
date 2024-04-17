#!/usr/bin/python3
"""Module: Student.

Has a Student class and it's methods.
"""


class Student():
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Sets the Student object necessary attributes.

        Args:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a Student instance dictionary representation."""
        return self.__dict__
