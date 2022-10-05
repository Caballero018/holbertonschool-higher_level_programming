#!/usr/bin/python3
"Module that has function that prints a text with \
2 new lines after each of these characters: ., ? and :"


def text_indentation(text):
    "Function that prints a text with 2 new lines after each \
of these characters: ., ? and :"
    if not text:
        return ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i - 1] == "." or text[i - 1] == ":" or text[i - 1] == "?":
            print()
            print()
        print(text[i], end="")
