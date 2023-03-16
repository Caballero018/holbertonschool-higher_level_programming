#!/usr/bin/python3
"Class Square that defines a square by: (based on 2-square.py)"


class Square:
    "Function with atrivute private"
    def __init__(self, size=0):
        self.__size = size

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

    def my_print(self):
        if self.__size == 0:
            print('')
            return

        sign_numb = ''
        for _ in range(self.__size):
            for _ in range(self.__size):
                sign_numb += '#'
            sign_numb += '\n'
        print(sign_numb, end='')
