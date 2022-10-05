#!/usr/bin/python3
""" Doc """


def text_indentation(text=""):
    """ Doc """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " ":
            if text[i - 1] == "?" or text[i - 1] == ":" or text[i - 1] == ".":
                print()
                print()
                continue
        else:
            if text[i - 1] == "?" or text[i - 1] == ":" or text[i - 1] == ".":
                print()
                print()
        print(text[i], end ="")
    if text[-1:] == "?" or text[-1:] == ":" or text[-1:] == ".":
        print()
        print()
