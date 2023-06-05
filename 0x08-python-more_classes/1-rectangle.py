#!/usr/bin/python3
""""This module defines class Rectangle"""


class Rectangle:
    """class defining rectangle by height or width"""
    def __init__(self, width=0, height=0):
        """Inistances class object
        Attributes:
            height (int): height of the rectangle.
            width (int): width of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """"Get the rectangl's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
