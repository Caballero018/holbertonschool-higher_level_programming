#!/usr/bin/python3
"Module that have a class with publics instances"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "Class with publics instances"
    def __init__(self, width, height):
        BaseGeometry.integer_validator(width, height)
        self.__width = width
        self.__height = height
