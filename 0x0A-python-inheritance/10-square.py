#!/usr/bin/python3
"""The class 'BaseGeometry' module"""


class BaseGeometry:
    """A class defining geometric class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the name and the value argument
        Arguments:
            name: value's name
            value: int > 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Class defining a rectangle"""
    def __init__(self, width, height):
        """Instance class object
        Arguments:
            width: Rectangle width
            height: Rectangle height
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """defines the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representin the object"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """A class that defines a square inherited from Rectangle"""
    def __init__(self, size):
        """Class object instance"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
