#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = []
    if my_list and search and replace:
        for i in range(len(my_list)):
            list.append(my_list[i])
            if list[i] == search:
                list[i] = replace
        return list
          