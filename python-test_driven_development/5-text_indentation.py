#!/usr/bin/python3
def text_indentation(text):
    if not text:
        return ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text) - 1):
        if text[i - 1] == "." or text[i - 1] == ":" or text[i - 1] == "?":
            print()
            print()
        print(text[i], end="")
