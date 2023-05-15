#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for alpha in my_string:
        if alpha not in ["c", "C"]:
            new_str = new_str + alpha
    return new_str
