#!/usr/bin/python3
"Module that have a class with publics instances"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "Class with publics instances"
    def __init__(self, width, height):
        if isinstance(width, int) and isinstance(height, int) and width > 0 and height > 0:
            self.__width = width
            self.__height = height
