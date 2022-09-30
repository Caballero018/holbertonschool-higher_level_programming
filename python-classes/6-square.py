#!/usr/bin/python3
"""This module define de class:Square with private instance attribute"""


class Square:
    """This method define a private instance attribute -> size"""
    def __init__(self, size=0, position=(0, 0)):
        """Define like Private instance attribute: size"""
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
    """New private instance attribute property"""
    @property
    def size(self):
        return self.__size

    """New private instance attribute property setter"""
    @size.setter
    def size(self, value):
        self.__size = value
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    """area is a new Public instance method"""
    def area(self):
        return self.__size * self.__size

    """my_print is a new Public instance method"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
