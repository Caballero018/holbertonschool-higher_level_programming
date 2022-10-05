#!/usr/bin/python3
""" Doc """


def add_integer(a, b=98):
    """ Doc """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    try:
        result = a + b
    except (OverflowError, ValueError):
        return 99
    if result == float('inf') or result == -float('inf'):
        raise OverflowError(89)
    return int(a) + int(b)
