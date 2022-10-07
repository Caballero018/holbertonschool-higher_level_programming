#!/usr/bin/python3
"Doc"


class Rectangle:
    "Doc"
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        
    @property
    def width(self):
        return self._Rectangle__width
    @width.setter
    def width(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            self._Rectangle__width = value
        else:
            raise TypeError("width must be an integer")
        
    @property
    def height(self):
        return self._Rectangle__height
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
