#!/usr/bin/python3
# tens range
for m in range(0, 10):
# ones range
    for n in range(m + 1, 10):
        print("{:d}".format(m), end="")
        if m == 8 and n  == 9:
            print("{:d}".format(n), end='\n')
        else:
            print("{:d}".format(n), end=', ')
