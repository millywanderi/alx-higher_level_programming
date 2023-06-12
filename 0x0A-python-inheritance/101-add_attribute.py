#!/usr/bin/python3
"""1101-add_attribute module"""


def add_attribute(obj, name, value):
    """Adds new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    else:
        setattr(obj, name, value)
