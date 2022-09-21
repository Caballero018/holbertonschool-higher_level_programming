#!/usr/bin/python3
i = 1
cont = 0
while i < 90:
    j = i % 10
    k = i / 10
    l = int(k)
    if j > l:
        if not (i == 89):
            print("{}{}" .format(l, j), end=", ")
        else:
            print("{}{}" .format(l, j))   
    i += 1
