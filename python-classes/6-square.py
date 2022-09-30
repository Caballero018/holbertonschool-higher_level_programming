#!/usr/bin/python3
"""
Add attribute in class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
    size(int): size of the square - private attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Property that retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter that sets the position"""
        mess = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(mess)

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(mess)

        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        size = self.__size
        whitespace = self.__position[1]
        rightspace = self.__position[0]

        if size == 0:
            print()

        for i in range(whitespace):
            print()

        for b in range(size):
            print((' ' * rightspace) + ('#' * size))
