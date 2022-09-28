#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i, val in a_dictionary.items():
        if i == key:
            a_dictionary[i] = value
        else:
            i, val = key, value
            a_dictionary[i] = val
        return a_dictionary
