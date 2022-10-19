#!/usr/bin/python3
"Module that have a class Rectangle that inherits from Base"
from models.base import Base


class Rectangle(Base):
    "Class Rectangle that inherits from Base"
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    "width"
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value

    "height"
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value

    "x"
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    "y"
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
