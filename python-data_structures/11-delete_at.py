#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list = []
    i = 0
    while i <= len(my_list) - 1:
        if not (i == idx):
            list.append(my_list[i])
        i += 1
    return list
