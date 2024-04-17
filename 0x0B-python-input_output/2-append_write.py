#!/usr/bin/python3
"""Module: append_write.

Defines a function appending a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF8 text file
    then returns the number of added characters.
    """
    with open(filename, 'a') as f:
        return f.write(text)
