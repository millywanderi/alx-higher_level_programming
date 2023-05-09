#!/usr/bin/python3
def remove_char_at(str, n):
    # check if the length is outside indices
    if n < 0 or n > len(str):
        return str
    # change to list
    arr = list(str)

    for m in range(0, len(str) - 1):
        if m > n:
            # take contents to the left side
            arr[m] = arr[m + 1]
    # combine components to form a string
    outcome = ''.join(arr)
    # truncate
    return outcome[:-1]
