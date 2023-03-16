#!/usr/bin/python3
"Class Square that defines a square by: (based on 2-square.py)"


class Square:
    "Function with atrivute private"
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    "Function with atrivute public"
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for number in value:
            if type(number) != int or number < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers'
                    )
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print('')
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print((' ' * self.__position[0]) + ('#') * self.__size)
