#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""


import sys
code = ['200', '300', '400', '401', '403', '404', '405', '500']
code_h = []
size_sum = 0
m = 0
try:
    for line in sys.stdin:
        toks = line.split(' ')
        size_sum += int(toks[-1])
        code_h.append(toks[-2])
        if m == 9:
            m = 0
            print("File size: " + str(size_sum))
            for cody in code:
                if cody in code_h:
                    print('{}: {}'.format(cody, code_h.count(cody)))
                else:
                    m += 1
except KeyboardInterrupt:
    print('File size: ' + str(size_sum))
    for cody in code:
        if cody in code_h:
            print('{}: {}'.format(cody, code_h.count(cody)))
    sys.exit()
