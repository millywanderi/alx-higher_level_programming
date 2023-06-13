#!/usr/bin/python3
"""This module writes an Object to a text file,
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """A function that def save_to_json_file(my_obj, filename)
    Arguments:
       my_object: Object
       filename: name
    """
    import json
    with open(filename, 'w', encoding='utf-8') as file_s:
        json.dump(my_obj, file_s)
