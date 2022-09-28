#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = {}
    for i, val in a_dictionary.items():
        if key == a_dictionary[i]:
            del a_dictionary[key]
        elif a == a_dictionary:
            return a_dictionary
        return a_dictionary