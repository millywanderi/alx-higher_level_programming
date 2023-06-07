#!/usr/bin/python3
"""This module divides all elements of a givene divisor"""


def matrix_divided(matrix, div):
    """divides a matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("dividsion by zero")
    x = len(matrix)
    ref_row = 0
    if x is not 0 and type(matrix[x - 1]) is list and len(matrix[x - 1]):
        ref_row = len(matrix[x - 1])
        n_matrix = [[] for row in range(x)]
    else:
        raise TypeError('matrix must be a matrix \
(lists of lists) of integers/floats')

    for row, n_row in zip(matrix, n_matrix):
        if type(row) is not list:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        if len(row) != ref_row:
            raise TypeError('Each row of the matrix must have the same size')
        for ele in row:
            if type(ele) is not float and type(ele) is not int:
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            n_row.append(round(float(ele / div), 2))
    return n_matrix
