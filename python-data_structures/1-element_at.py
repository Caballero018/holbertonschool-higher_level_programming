#!/usr/bin/python3
def element_at(my_list, idx):
    if not (idx < 0 or idx > len(my_list)):
        return my_list[idx]
    return "None"