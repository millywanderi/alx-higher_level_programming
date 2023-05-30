#!/usr/bin/python3
"""This module defines an empty class square"""


class Square:

    """A class defining a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates class attributes

        Attributes:
             size (int): size of square
             position (int, int): New square position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets class private attribute to be used"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self, value):
        """Gets class private attribute to be used"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or
                len(value) != 2 or
                not all((isinstance(number, int) for number in value) or
                not all((number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """prints square in form of # stdout"""
        if self.__size == 0:
            print()
            return

        [print("") for m in range(0, self.__position[1])]
        for m in range(0, slef.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define square representation while printing"""
        if self.__size != 0:
            [print("") for m in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            if m != self.__size - 1:
                print("")
        return ("")
