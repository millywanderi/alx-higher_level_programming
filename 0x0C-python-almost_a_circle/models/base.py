#!/usr/bin/python3
"""
This module defines a class base
"""

import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_cls = cls(1, 1)
        else:
            new_cls = cls(1, 1)
        new_cls.update(**dictionary)
        return new_cls

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json") as file:
                obj = cls.from_json_string(file.read())
            for a, b in enumerate(obj):
                obj[a] = cls.create(**b)
        except IOError:
            return []
        return obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        lists = list_objs
        if not lists:
            lists = []
        new_lists = []
        for i in lists:
            new_lists.append(i.to_dictionary())
        keys = [[j for j in k.keys()] for k in new_lists]

        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as file:
            writing = csv.DictWriter(file, fieldnames=keys[0])
            writing.writeheader()
            writing.writerows(new_lists)

    @classmethod
    def load_from_file_csv(cls):
        dic = {}
        lists = []
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as file:
                reading = csv.reader(file)
                key_value = reading.__next__()

                for n in reading:
                    for a, b in zip(key_value, n):
                        dic[a] = int(b)
                    lists.append(cls.create(**dic))

        except IOError:
            return []
        return lists
