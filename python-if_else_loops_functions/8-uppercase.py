#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            char = ord(char) - 32
            char = chr(char)
        print(char, end="")
    print()
