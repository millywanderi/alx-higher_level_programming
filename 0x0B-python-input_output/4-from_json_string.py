#!/usr/bin/python3
"""This module returns an object represented by json str"""


def from_json_string(my_str):
    """A function that returns an object represented by json str
    Arguments:
        my_str: string
    """
    import json
    return json.loads(my_str)
