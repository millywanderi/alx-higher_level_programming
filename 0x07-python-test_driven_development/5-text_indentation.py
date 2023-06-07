#!/usr/bin/python3
"""
5-text_indentation module
"""


def text_indentation(text):
    """
    prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    lists_lines = [lines.strip(' ') for lines in text.split('\n')]
    revise = "\n".join(lists_lines)
    print(revise, end='')
