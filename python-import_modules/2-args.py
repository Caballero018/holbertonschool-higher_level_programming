#!/usr/bin/python3
from ast import arg
from sys import argv
if __name__ == "__main__":
    ar = len(argv) - 1
    i = 1
    if ar <= 0:
        print("{} arguments." .format(ar))
    else:
        print("{} arguments:" .format(ar))
        while i <= ar:
            if i == 1:
                print("{}: {}".format(i, argv[i]), end=" ")
            else:
                print("{}: {}".format(i, argv[i]))
            i += 1
