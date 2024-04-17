#!/usr/bin/python3
"""Module: write_file.

Defines a function that inserts a text line to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts text line to a file, after
    each line containing a specific string.
    """
    output = ""
    with open(filename, 'r') as f:
        for line in f:
            output += line
            if search_string in line:
                output += new_string

    with open(filename, 'w') as f:
        f.write(output)
