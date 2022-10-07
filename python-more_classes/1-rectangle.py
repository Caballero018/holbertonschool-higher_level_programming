#!/usr/bin/python3
"Doc"


class Rectangle:
    "Doc"
    def __init__(self, width, height):
        self.height = height
        self.width = width
        
    @property
    def width(self):
        return self._Rectangle__width
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self._Rectangle__width = value
    @property
    def height(self):
        return self._Rectangle__height
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self._Rectangle__height = value
