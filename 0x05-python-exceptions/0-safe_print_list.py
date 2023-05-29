#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    amnt = 0
    try:
        for m in range(x):
            print("{}".format(my_list[m]), end='')
            amnt += 1
    except IndexError:
        pass
    print()
    return (amnt)
