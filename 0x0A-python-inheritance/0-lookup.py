#!/usr/bin/python3
"""Module: MyList.

Contains a class that inherits from a list
and a sorted list method to print.
"""


class MyList(list):
    """MyList class definition."""

    def print_sorted(self):
        """sorted list print function."""
        print(sorted(self))
