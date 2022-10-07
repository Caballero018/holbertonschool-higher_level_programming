#!/usr/bin/python3
"Doc"


class Rectangle:
    "Doc"
    def __init__(self, width=0, height=0):
        self._Rectangle__width = width
        self._Rectangle__height = height
    
    def width(self, value):
        value = self._Rectangle__width
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
    def height(self, value):
        value = self._Rectangle__height
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
