#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = len(my_list) - 1 
    list = my_list
    for i in range(len(my_list)):
        my_list[i] = list[j]
        print("{:d}" .format(my_list[i]))
        j -= 1
