#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argue = len(argv) - 1
    if argue > 1:
        print("{:d} arguments:".format(argue))
    elif argue == 1:
        print("1 argument:".format(argue))
    else:
        print("0 arguments.".format(argue))

    num = 1
    for m in argv[1:]:
        print("{:d}: {:s}".format(num, m))
        num += 1
