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
