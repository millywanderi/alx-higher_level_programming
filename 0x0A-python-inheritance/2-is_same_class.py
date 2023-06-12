#!/usr/bin/python3
"""Class module testing object as a class instance"""


def is_same_class(obj, a_class):
    """Check if an object is exactly a class
    Arguments:
        obj: test object
        a_class: class to be tested
    """
    if type(obj) == a_class:
        return True
    else:
        return False
