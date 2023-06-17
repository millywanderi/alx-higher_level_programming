#!/usr/bin/python3
"""
This module defines a class base
"""

import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        dictionaries = json.dumps(list_dictionaries)
        return dictionaries

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        saving = []
        for x in list_objs:
            saving.append(cls.to_dictionary(x))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(saving))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        dic = json.loads(json_string)
        return dic
