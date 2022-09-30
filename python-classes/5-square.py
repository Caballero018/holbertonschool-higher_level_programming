#!/usr/bin/python3
"""
Add print method in class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
    size(int): size of the square - private attribute.
    """

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        size = self.__size

        if size == 0:
            print()

        for i in range(size):
            print('#' * size)

    @property
    def size(self):
        """Property that retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter that sets the value of size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
