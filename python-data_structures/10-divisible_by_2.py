#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tr = [True, False]
    for i in my_list:
        if i % 2 == 0:
            return tr[0]
        else:
            return tr[1]
