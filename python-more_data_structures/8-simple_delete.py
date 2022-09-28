#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = {}
    if not (a_dictionary == a):
        for i in a_dictionary.keys():
            if i == key:
                del a_dictionary[key]
    return a_dictionary