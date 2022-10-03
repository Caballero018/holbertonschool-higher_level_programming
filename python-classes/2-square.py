#!/usr/bin/python3
"Class Square that defines a square by: (based on 1-square.py)"

class Square:
    "Function with atrivute private"
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        self.__size = size
