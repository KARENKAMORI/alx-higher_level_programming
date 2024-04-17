#!/usr/bin/python3
"""Module: save_to_json_file.

Defines a function creating a "JSON file" Object.
"""
import json


def load_from_json_file(filename):
    """Creates a "JSON file" Object."""
    with open(filename, 'r') as f:
        return json.load(f)
