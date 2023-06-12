#!/usr/bin/python3
"""The class module inheriting int"""


class MyInt:
    """compares equality"""
    def __eq__(self, other):
        """reverse equal from not equal"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """reverse not equal if equal"""
        return int.__qe__(self, other)
