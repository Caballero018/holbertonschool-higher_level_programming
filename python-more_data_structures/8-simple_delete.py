#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = {}
    if not (a_dictionary == a):
        if a_dictionary[key]:
            del a_dictionary[key]
    return a_dictionary