#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = len(my_list)
    list = []
    
    for i in range(len(my_list) - 1):
        list[i] = my_list[j]
        print("{:d}" .format(list[i]))
        j -= 1
    