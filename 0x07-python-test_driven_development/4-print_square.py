#!/usr/bin/python3
"""Print square Module
prints using # character
"""


def print_square(size):
    """Prints a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for m in range(size):
        for n in range(size):
            print("#", end='')
        print()
