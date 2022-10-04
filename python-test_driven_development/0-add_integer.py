#!/usr/bin/python3
"Function that adds 2 integers."

def add_integer(a, b=98):
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not a  or not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not b or not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, int) or isinstance(b, int):
        return a + b

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
