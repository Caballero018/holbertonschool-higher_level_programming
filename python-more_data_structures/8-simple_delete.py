#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = {}
    if not (a_dictionary == a):
        for i in a_dictionary.keys():
            if not (i == key):
                return a_dictionary                    
        del a_dictionary[key]
        return a_dictionary