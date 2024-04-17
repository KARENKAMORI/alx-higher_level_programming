#!/usr/bin/python3
"""Module: read_file.

Has a function that reads a text file.
"""


def read_file(filename=""):
    """Reads a UTF8 text file and prints it to stdout."""
    with open(filename, 'r') as f:
        print(f.read(), end='')
