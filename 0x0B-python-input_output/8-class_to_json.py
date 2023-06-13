#!/usr/bin/python3
"""This module returns the dictionary description"""


def class_to_json(obj):
    """a function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    Arguments:
        obj: object
    """
    return obj.__dict__
