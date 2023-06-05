#!/usr/bin/python3
"""This module defines class Rectangle"""


class Rectangle:
    """class defining rectangle by height or width"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiates class object
        Attributes:
            height (int): height of the rectangle.
            width (int): width of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """"Get the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles by area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def area(self):
        """Returns the rectangle's area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """clas object represented by a string"""
        sln = ""
        if self.__width == 0 or self.__height == 0:
            return sln
        else:
            str_symbol = str(self.print_symbol)
            for m in range(self.__height - 1):
                sln += (str_symbol * self.__width) + '\n'
            sln += str_symbol * self.__width
        return sln

    def __repr__(self):
        """Code representation of instance"""
        hei = str(self.__height)
        wid = str(self.__width)
        sln = "Rectangle(" + wid + ", " + hei + ")"
        return sln

    def __del__(self):
        """Delete instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
