#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = len(my_list)
    list = []
    
    for i in range(len(my_list)):
        my_list[i] = list[j]
        j -= 1