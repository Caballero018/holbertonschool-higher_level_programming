#!/usr/bin/python3
def islower(c):
    s, d = 'a', 'z'
    if not (ord(c) <= d and ord(c) >= s):
        return False
    return True
