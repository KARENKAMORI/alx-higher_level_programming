#!/usr/bin/python3
"""Module: add_attribute.

Contains a checking function.
"""


def add_attribute(obj, name, value):
    """If it's possible, Adds a new attribute to an object."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
