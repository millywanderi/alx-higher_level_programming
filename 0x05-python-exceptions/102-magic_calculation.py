#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too Far')
            res += (a ** b) / m
        except Exception:
            res = b + a
            break
    return res
