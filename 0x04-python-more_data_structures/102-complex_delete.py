#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_del = []
    for fung, dham in a_dictionary.items():
        if dham is value:
            key_del.append(fung)
    if len(key_del) > 0:
        for dels in key_del:
            del a_dictionary[dels]
    return a_dictionary
