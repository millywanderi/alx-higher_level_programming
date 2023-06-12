#!/usr/bin/python3
"""Class module testing if an object is an instance
of inherited class
"""


def is_kind_of_class(obj, a_class):
    """Test if an object is an instance a specified class

    Arguments:
        obj: test object
        a_class: class to be tested
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
