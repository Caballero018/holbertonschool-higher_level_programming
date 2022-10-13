#!/usr/bin/python3
"Module that have a function that returns the list of available \
attributes and methods of an object"


def lookup(obj):
    "Function that returns the list of available \
    attributes and methods of an object"
    obj = dir(obj)
    return obj
