#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    list = str(matrix)
    d = ""
    for i in list:
        if not (i == ',' or i == '[' or i == ']'):
            d += i
            
    for s in range(len(d)):
        if d[s] == '4' or d[s] == '7':
            print()
        print(d[s], end="")
    print()

