#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    ar = len(argv)
    x = 0
    i = 1
    for i in range(1, ar):
        x += int(argv[i])
    print(x)