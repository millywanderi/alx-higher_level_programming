#!/usr/bin/python3
"""Define MagicClass performing task exacly like bytecode"""


import math


class MagicClass:
    def __init__(self, radius=0):
        """Instantiates MagicClass
        Attributes:
            radius (float or int): New MagicClass radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """"Returns MagicClass area"""
        return (self.__radius ** 2 * mat.pi)

    def circumference(self):
        """Return MagicClass circumference"""
        return (2 * math.pi * self.__radius)
