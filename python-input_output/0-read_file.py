#!/usr/bin/python3
"Module that have a function that reads a \
text file (UTF8) and prints it to stdout"


def read_file(filename=""):
    "Function that reads a text file (UTF8) and prints it to stdout"
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
