#!/usr/bin/python3
"""Module: Lookup.

Contains a function that returns a list of
available object attributes and methods
"""


def lookup(obj):
    """Returns list of available object attributes and methods"""
    return dir(obj)
