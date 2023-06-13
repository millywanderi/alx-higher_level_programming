#!/usr/bin/python3
"""A module that reads a file and prints its contents"""


def read_file(filename=""):
    """A function reading the file and prints to stdout"""
    with open(filename, 'r', encoding="utf_8") as f:
        ptint(f.read(), end='')
