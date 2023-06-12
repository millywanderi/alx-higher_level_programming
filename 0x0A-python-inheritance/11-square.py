#!/usr/bin/python3
"""The class 'BaseGeometry' module and Rectangle subclass"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class
        Arguments:
            size: square size
    """
    def __init__(self, size):
        """square instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return area"""
        return super().area()

    def __str__(self):
        """prints the square"""
        return "[square] {:d}/{:d}".format(self.__size, self.__size)
