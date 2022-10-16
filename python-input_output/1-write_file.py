#!/usr/bin/python3
"Module that have a function that writes a string to a text file \
(UTF8) and returns the number of characters written"


def write_file(filename="", text=""):
    "Function that writes a string to a text file (UTF8) and \
    returns the number of characters written"
    with open(filename, mode="w", encoding="utf-8") as f:
        write_file = f.write(text)
    print(len(text))
