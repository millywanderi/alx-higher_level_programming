#!/usr/bin/python3
"""This module writes a string and returns characters"""


def write_file(filename="", text=""):
    """A function that writes file and return no. of char"""
    with open(filename, 'w', encoding='utf-8') as file_w:
        return file_w.write(text)
