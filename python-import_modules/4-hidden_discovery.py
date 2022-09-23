#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    s = str(dir(hidden_4))
    d = ""
    for i in s:
        if not(i == '\'' or i == '[' or i == ']' or i == ','):
            d += i
    d = d.split()
    i = 9
    while i < len(d):
        print(d[i], end="\n")
        i += 1
