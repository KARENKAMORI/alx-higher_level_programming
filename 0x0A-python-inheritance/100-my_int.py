#!/usr/bin/python3
"""Module: MyInt.

Contains an int inheriting class.
"""


class MyInt(int):
    """Defines MyInt class."""

    def __eq__(self, other):
        """== behaviour setting."""
        return int(self) != other

    def __ne__(self, other):
        """!= behaviour setting."""
        return int(self) == other
