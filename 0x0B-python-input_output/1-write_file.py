#!/usr/bin/python3
"""Module: write_file.

Defines a function writing to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF8 text file then
    returns the number of written characters.
    """
    with open(filename, 'w') as f:
        return f.write(text)
