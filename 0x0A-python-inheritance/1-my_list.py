#!/usr/bin/python3
"""Class module inheriting a class from list"""


class MyList(list):
    """Class inheriting from list"""
    def print_sorted(self):
        """sorts a lists in an ascending order"""
        print(sorted(self))
