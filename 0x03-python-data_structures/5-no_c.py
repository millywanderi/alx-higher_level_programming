#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        new_str = my_string.translate({ord(ch): None for ch in "cC"})
        return new_str
