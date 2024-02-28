#!/usr/bin/python3
"""Program defining a matrix function"""

def matrix_divided(matrix, div):
    """Deviding all matrix elements
    Args:
        matrix (list): A list of float or int lists.
        div (int/float): Devisor.
    Raises:
        TypeError: If non-numbers in matrix
        TypeError: If different row sizes in matrix.
        TypeError: Non-float or non-int div.
        ZeroDivisionError: if 0 div.
    Return:
        New matrix representing division results.
    """

    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix and not isinstance(matrix, list):
        raise TypeError(errorMessage)

    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int):
                raise TypeError(errorMessage)
            if not isinstance(item, float):
                raise TypeError(errorMessage)

    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in lists] for lists in matrix]
