#!/usr/bin/python3
"""This module creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”
    Arguments:
        filename: json file name
    """
    import json
    with open(filename, 'r', encoding='utf-8') as file_l:
        return json.load(file_l)
