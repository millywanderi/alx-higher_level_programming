#!/usr/bin/python3
"""This module appends a string at the end of txt file"""


def append_write(filename="", text=""):
    """Appends text file str and returns
    number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file_a:
        return file_a.write(text)
