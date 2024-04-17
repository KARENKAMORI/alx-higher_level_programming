#!/usr/bin/python3
"""Module: save_to_json_file.

Defines a function writing an Object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """Uses JSON representation to write an Object to a text file."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
