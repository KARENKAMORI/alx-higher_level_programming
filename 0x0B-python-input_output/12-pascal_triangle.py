#!/usr/bin/python3
"""Module: pascal_triangle.

Defines a function returning a list of lists of
integers representing the n Pascal’s triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the n Pascal’s triangle.
    """
    if n <= 0:
        return []

    res = [[1]]
    while len(res) is not n:
        temp = [1]
        for i in range(len(res[-1]) - 1):
            temp.append(res[-1][i] + res[-1][i + 1])
        temp.append(1)
        res.append(temp)
    return res
