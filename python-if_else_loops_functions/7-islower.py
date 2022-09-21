#!/usr/bin/python3
def islower(c):
    s, d = 'a', 'z'
    if not (c <= d and c >= s):
        return False
    elif not (c == ''):
        return True
