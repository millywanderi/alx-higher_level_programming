#!/usr/bin/python3
"""The class module inheriting int"""


class MyInt:
    """compares equality"""
    def __eq__(self, other):
        """reverse equal from not equal"""
        if self is not other:
            return True
        else:
            return False

    def __ne__(self, other):
        """reverse not equal if equal"""
        if self is not other:
            return True
        else:
            return False
