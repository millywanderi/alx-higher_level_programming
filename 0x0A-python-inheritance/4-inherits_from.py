#!/usr/bin/python3
"""Class module testing if an object is directly or indirectly
inherited from a specified class
"""


def inherits_from(obj, a_class):
    """Test if an object is directly or indirectly
    inherited

    Arguments:
        obj: test object
        a_class: class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
