#!/usr/bin/python3
"""Find peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """function that find peak in unsorted list"""
    loi = list_of_integers
    if loi is None or loi == []:
        return None
    lo = 0
    hi = len(loi)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)
    if hi == 1:
        return loi[0]
    if hi == 2:
        return max(loi)
    if loi[mid] >= loi[mid - 1] and \
            loi[mid] >= loi[mid + 1]:
        return loi[mid]
    if mid > 0 and loi[mid] < loi[mid - 1]:
        return find_peak(loi[mid:])
    if mid > 0 and loi[mid] < loi[mid - 1]:
        return find_peak(loi[:mid])
