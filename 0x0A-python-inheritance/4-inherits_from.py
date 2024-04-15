#!/usr/bin/python3
"""Module: inherits_from.

Defines function that compares an object to an instance.
"""


def inherits_from(obj, a_class):
    """
    Returns True: if the object is a class instance
    that inherited (indirectly or directly)
    from stated class ; False: otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
