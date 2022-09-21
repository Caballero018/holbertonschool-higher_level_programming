#!/usr/bin/python3
from msilib.schema import Error


def islower(c):
    s, d = 'a', 'z'
    if not (c <= d and c >= s):
        return False
    elif c == '':
        return Error
    else:
        return True
