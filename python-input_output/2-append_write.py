#!/usr/bin/python3
"Module that have function that appends a string at the end \
of a text file (UTF8) and returns the number of characters added"


def append_write(filename="", text=""):
    "Function that appends a string at the end of a text file (UTF8) \
    and returns the number of characters added"
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
    return len(text)
