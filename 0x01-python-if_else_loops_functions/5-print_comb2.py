#!/usr/bin/python3
for m in range(0, 100):
    if m != 99:
        print("{:02d}, ".format(m), end="")
    else:
        print("{:02d}".format(m))
