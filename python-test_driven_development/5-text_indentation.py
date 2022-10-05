#!/usr/bin/python3
""" Doc """


def text_indentation(text="as"):
    """ Doc """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " " or text[i] != " ":
            if (text[i - 1] == "?" or text[i - 1] == ":" or text[i - 1] == ".") and text[i] == " ":
                print()
                print()
                if text[i] == " ":
                    continue
            print(text[i], end="")
    if text[-1:] == "?" or text[-1:] == ":" or text[-1:] == ".":
        print()
        print()
