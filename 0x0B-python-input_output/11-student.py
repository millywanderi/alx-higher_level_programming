#!/usr/bin/python3
"""This is a student class module"""


class Student():
    """Class defining a student"""
    def __init__(self, first_name, last_name, age):
        """Instances class student
        Arguments:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)
        """
        key_valid = []
        dict_return = {}
        if type(attrs) is list:
            for ele in attrs:
                if type(ele) is str and ele in self.__dict__:
                    dict_return.update({ele: self.__dict__[ele]})
            return dict_return
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if len(json) != 0:
            self.__dict__ = json
