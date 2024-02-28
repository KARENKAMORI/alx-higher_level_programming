#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """matrix multiplication.

    Args:
        m_a: matrix one.
        m_b: matrix two.
    Raises:
        TypeError: If arguments are not a list of ints/floats lists.
        TypeError: If either of the args are empty.
        TypeError: If either of the args have different-sized rows.
        ValueError: If args cannot be multiplied.
    Returns:
        m_a by m_b matrix multiplication.
    """

    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for i in range(len(m_b[0])):
        row_new = []
        for j in range(len(m_b)):
            row_new.append(m_b[j][i])
        inverted_b.append(row_new)

    matrix_new = []
    for r in m_a:
        row_new = []
        for c in inverted_b:
            mul = 0
            for i in range(len(inverted_b[0])):
                mul += r[i] * c[i]
            row_new.append(mul)
        matrix_new.append(row_new)

    return matrix_new
