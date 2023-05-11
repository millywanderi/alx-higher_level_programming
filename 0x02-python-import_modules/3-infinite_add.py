#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argue = len(sys.argv) - 1

    if argue == 0:
        print("{}".format(argue))
    elif argue == 1:
        print("{}".format(sys.argv[argue]))
    elif argue > 1:
        sum = 0
        for m in argv[1:]:
            sum += int(m)
    print(sum)
