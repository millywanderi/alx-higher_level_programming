#!/usr/bin/python3
""" Add two numbers and returns their result """


def add_integer(a, b=98):
    """ Add two numbers and returns their result """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)
    return a + b
