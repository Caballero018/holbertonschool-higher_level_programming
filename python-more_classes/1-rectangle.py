#!/usr/bin/python3
"Doc"


class Rectangle:
    "Doc"
    def __init__(self, width, height):
        self._Rectangle__height = height
        self._Rectangle__width = width

        if type(self._Rectangle__width) is not int:
            raise TypeError("width must be an integer")
        if self._Rectangle__width < 0:
            raise ValueError("width must be >= 0")
        
        if type(self._Rectangle__height) is not int:
            raise TypeError("height must be an integer")
        if self._Rectangle__height < 0:
            raise ValueError("height must be >= 0")
