#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if not (i == "c" and i == "C"):
            d = i
            print(d, end = "")
