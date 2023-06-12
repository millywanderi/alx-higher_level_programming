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
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False
