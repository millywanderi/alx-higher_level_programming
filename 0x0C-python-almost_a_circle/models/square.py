#!/usr/bin/python3
"""
This is a clas module defining class square inherited from Rectangle
"""


from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.__size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        length = len(args)
        if length != 0 and args is not None:
            for a, arg in enumerate(args):
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.size = arg
                if a == 2:
                    self.x = arg
                if a == 3:
                    self.y == arg
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        dic = ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            })
        return dic
