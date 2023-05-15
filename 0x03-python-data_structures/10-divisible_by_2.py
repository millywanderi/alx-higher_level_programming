#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lists = []
    length = len(my_list)
    for m in my_list(length):
        if (my_list[m] % 2) == 0:
            lists.append(True)
        lists.append(False)
    return lists
