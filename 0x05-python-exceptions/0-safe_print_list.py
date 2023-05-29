#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    amnt = 0
    for m in range(x):
        try:
            print(my_list[m], end='')
        except IndexError:
            x = m
        finally:
            print()
            return x
