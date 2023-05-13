#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    i = my_list[0]
    for m in range(1, (len(my_list))):
        if my_list[m] > i:
            i = my_list[m]
    return i
