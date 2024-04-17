#!/usr/bin/python3
"""class_to_json module.

Contains a function that returns a dictionary.
"""


def class_to_json(obj):
    """
    Returns a description dictionary with simple data
    structure (dictionary, integer, list, string and boolean)
    for object JSON serialization.
    """
    return obj.__dict__
