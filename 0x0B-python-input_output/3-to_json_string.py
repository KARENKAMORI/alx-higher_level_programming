#!/usr/bin/python3
"""Module: to_json_string.

Defines a function that returns the object's JSON representation.
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of a string object."""
    return json.dumps(my_obj)
