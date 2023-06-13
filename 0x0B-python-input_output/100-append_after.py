#!/usr/bin/python3
"""This module inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    lists = []
    with open(filename, 'r', encoding='utf-8') as file_a:
        for line in file_a:
            lists += [line]
            if line.find(search_string) != -1:
                lists += [new_string]

    with open(filename, 'w', encoding='utf-8') as file_w:
        file_w.write("".join(lists))
