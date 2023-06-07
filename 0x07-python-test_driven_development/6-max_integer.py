#!/usr/bin/python3
"""
max_integer module
"""


def max_integer(list=[]):
    """maximum integer function"""
    if len(list) == 0:
        return None
    res = list[0]
    m = 1
    while m < len(list):
        if list[m] > res:
            res = list[m]
        m += 1
    return res
