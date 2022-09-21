#!/usr/bin/python3
i = 0
while i < 100:
    j = i % 10
    k = i / 10
    l = str(k)
    if not (i == 99):
        print("{}{}" .format(l[0], j), sep="", end=", ")
    else:
        print("{}{}" .format(l[0], j))
    i += 1

