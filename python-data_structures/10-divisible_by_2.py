#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # list() sirve para crear nueva lista
    new_list = list()
    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            # .append es para agregar algo al final de una lista
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
