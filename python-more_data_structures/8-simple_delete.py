#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = {}
    if not (a_dictionary == a):
        for i, val in a_dictionary.items():
            if key == a_dictionary[i]:
                del a_dictionary[key]
            return a_dictionary