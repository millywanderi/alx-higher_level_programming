#!/usr/bin/python3
"""Find peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """function that find peak in unsorted list"""
    loi = list_of_integers
    size = len(loi)

    if size == 0:
        return None

    if size == 1:
        return loi[0]

    if loi[0] >= loi[1]:
        return loi[0]

    if loi[size - 1] >= loi[size - 2]:
        return loi[size - 1]

    # Binary search for the peak
    fro = 1
    ahead = size - 2

    while fro <= ahead:
        mid = (fro + ahead) // 2

        if loi[mid - 1] > loi[mid] and \
                loi[mid] >= loi[mid + 1]:
            return loi[mid]

        elif loi[mid - 1] > loi[mid]:
            ahead = mid - 1
        else:
            fro = mid + 1

    return None
