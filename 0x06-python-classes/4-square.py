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
        self.size = size

    @property
    def size(self):
        """Gets class attribute to be used"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2
