#!/usr/bin/python3
"""Module that have a class with publics instances"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class with publics instances"""
    def __init__(self, width, height):
        self.integer_validator(width, width)
        self.integer_validator(height, height)
        self.__height = height
        self.__width = width
