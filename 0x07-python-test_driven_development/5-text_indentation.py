#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """text indent
    Args:
        text: Text to be printed.
    Raises:
        TypeError: Non-string text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in "?:.":
        words = (i + "\n\n").join(
                [n.strip(" ") for n in words.split(i)])
