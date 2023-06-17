#!/usr/bin/python3
"""
This is a Rectangle modue that inherits from Base Class
"""


from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for q in range(self.__y):
            print()
        for m in range(0, self.__height):
            for n in range(0, self.__x):
                print(" ", end='')
            print("#" * self.__width)

    def __str__(self):
        m = str(self.id)
        n = str(self.__x)
        p = str(self.__y)
        q = str(self.__width)
        s = str(self.__height)
        return ("[Rectangle] (" + m + ") " + n + "/" + p + " - " + q + "/" + s)

    def update(self, *args, **kwargs):
        length = len(args)
        if length > 0 and args is not None:
            for a, arg in enumerate(args):
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.width = arg
                if a == 2:
                    self.height = arg
                if a == 3:
                    self.x = arg
                if a == 4:
                    self.y = arg
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        dic = ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            })
        return dic
