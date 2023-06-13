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

    def to_json(self):
        """a function that retrieves dictionary representation"""
        return self.__dict__
