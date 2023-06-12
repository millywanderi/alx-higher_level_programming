#!/usr/bin/python3
"""Class module inheriting a class from list"""


class MyList(list):
    """Class inheriting from list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """sorts and prints list in an ascending order"""
        print(sorted(self))
