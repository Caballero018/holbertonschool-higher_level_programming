#!/usr/bin/python3
"Doc"


class Rectangle:
    "Doc"
    def __init__(self, width, height):
        self._Rectangle__height = height
        self._Rectangle__width = width

        value = self._Rectangle__width
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        value_2 = self._Rectangle__height
        if type(value_2) is not int:
            raise TypeError("height must be an integer")
        if value_2 < 0:
            raise ValueError("width must be >= 0")
