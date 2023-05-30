#!/usr/bin/python3
"""This module defines an empty class square"""


class Square:

    """A class defining a square"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        Instantiates class attributes

        Attributes:
             size: size of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets class private attribute to be used"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets class private attribute to be used"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints square in form of # stdout"""
        if self.__size == 0:
            print()
        else:
            position1, position2 = self.__position
            num = 0

            for m in range(position2):
                print()
            while num < self.__size:
                n = 0
                while n < position1:
                    print(" ", end='')
                    n += 1

                numeral = 0

                while numeral < self.__size:
                    print("{}".format("#"), end='')
                    numeral += 1
                print()
                num += 1
