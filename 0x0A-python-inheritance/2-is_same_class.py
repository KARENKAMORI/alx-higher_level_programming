#!/usr/bin/python3
"""Module: is_same_class.

Defines a function that compares an object to an instance.
"""


def is_same_class(obj, a_class):
    """
    Returns True: if the object is an exact instance
    of the specified class ; False: otherwise.
    """
    return type(obj) is a_class
