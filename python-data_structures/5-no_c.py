#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in my_string:
        if not (i == "c" or i == "C"):
            str += i
    return str
