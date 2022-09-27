#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        my_list = None
        return my_list
    else:
        max = my_list[0]
        for i in my_list:
            if i > max:
                max = i
        return max
    
