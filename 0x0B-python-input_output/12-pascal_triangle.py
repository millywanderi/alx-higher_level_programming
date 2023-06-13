#!/usr/bin/python3
"""This module returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """A function returning pascal's triangle"""
    mat = []
    ini = []
    for m in range(n):
        lists = []
        row = -1
        col = 0

        for a in range(len(ini) + 1):
            if row == -1 or col == len(ini):
                lists += [1]
            else:
                lists += [ini[row] + ini[col]]
            row += 1
            col += 1
        mat.append(lists)
        ini = lists[:]
    return mat
