#!/usr/bin/python3
def islower(c):
    s, d = 'a', 'z'
    if ord(c) <= 97 and ord(c) >= 122:
        return True
    return False
