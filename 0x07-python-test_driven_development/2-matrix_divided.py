#!/usr/bin/python3
"""Defines a function that divides a matrix"""


def matrix_divided(matrix, div):
    """Divides each element in matrix by div

    Args:
        matrix: list to be paresd
        div: divisor in this sense
    Raises:
        TypeError: if matrix isn't a list of integers or floats
        TypeError: if rows of matrix aren't of the same size
        TypeError: if div is not a number(integer, float)
        ZeroDivisionError: if div is zero
    """

    # checks the type of each element in matrix against int, float
    message = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message)

    # checks size of rows in list
    elementInRowNum = {}
    i = 0
    j = 0
    for row in matrix:
        for element in row:
            i += 1
        elementInRowNum['row' + str(j)] = i
        j += 1
        i = 0

    val = sorted(list(elementInRowNum.values()))
    for i in range(len(val)):
        if val[i] < val[i + 1]:
            raise TypeError("Each row of the matrix must have the same size")
        break

    # check type of div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check for value of div if zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMatrix = [[round(element / div, 2) for element in row]for row in matrix]
    return newMatrix
