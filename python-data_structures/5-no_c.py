#!/usr/bin/python3
def no_c(my_string):
    j = len(my_string) - 1
    if not (my_string == None):
        for i in my_string[j]:
            if not (i == "c" or i == "C"):
                print(i, end = "")
