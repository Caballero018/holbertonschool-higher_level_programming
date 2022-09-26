#!/usr/bin/python3
def no_c(my_string):
    if not (my_string == None):
        for i in my_string:
            if not (i == "c" or i == "C"):
                print(i, end = "")
