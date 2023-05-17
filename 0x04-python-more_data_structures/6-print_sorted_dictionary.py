#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = sorted(a_dictionary)
    for m in ordered_keys:
        print("{}: {}".format(m, a_dictionary[m]))
