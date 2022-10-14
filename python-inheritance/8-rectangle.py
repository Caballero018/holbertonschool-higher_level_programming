#!/usr/bin/python3
"Module that have a class with publics instances"
from ctypes import sizeof


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if isinstance(width, sizeof) and isinstance(height, sizeof):
            self.__width = width
            self.__height = height
