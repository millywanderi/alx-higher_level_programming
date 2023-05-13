#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a < 2:
        if len_a == 0:
            c = 0
            d = 0
        elif len_a == 1:
            c = tuple_a[0]
            d = 0
    else:
        c = tuple_a[0]
        d = tuple_a[1]

    if len_b < 2:
        if len_b == 0:
            i = 0
            j = 0
        elif len_b == 1:
            i = tuple_b[0]
            j = 0
    else:
        i = tuple_b[0]
        j = tuple_b[1]

    tuple_new = (c + i, d + j)
    return tuple_new
