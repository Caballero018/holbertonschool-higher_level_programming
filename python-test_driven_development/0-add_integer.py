#!/usr/bin/python3
"Function that adds 2 integers."


def add_integer(a, b=98):
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if a == None or not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if b ==  None or not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, int) or isinstance(b, int):
        return a + b
