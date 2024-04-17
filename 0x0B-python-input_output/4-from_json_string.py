#!/usr/bin/python3
"""Module: from_json_string.

Defines a function that returns a JSON string representing an object.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python data structure object
    representing a JSON string:.
    """
    return json.loads(my_str)
