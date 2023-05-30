#!/usr/bin/python3
"""This module defines an empty class square"""


class Square:

    """A class defining a square"""

    def __init__(self, size=0) -> None:
        """
        Instantiates class attributes

        Attributes:
             size: size of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2
