#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = {}
    if a_dictionary != a:
        for i in a_dictionary.keys():
            if key == a_dictionary[i]:
                del a_dictionary[key]
            return a_dictionary
    
    
    
    