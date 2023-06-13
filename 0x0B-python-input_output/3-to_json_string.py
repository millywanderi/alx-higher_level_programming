#!/usr/bin/python3
"""This module returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """A function that returns the JSON
    representation of an object (string)
    Arguments:
        my_obj: Object
    """
    import json
    return json.dumps(my_obj)
