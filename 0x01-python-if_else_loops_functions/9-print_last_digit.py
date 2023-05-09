#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1

    tmp = number % 10
    print("{:d}".format(tmp), end="")
    return tmp
