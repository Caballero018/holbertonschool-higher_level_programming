#!/usr/bin/python3
"Module that have a class MyList that inherits from list"


class MyList(list):
    "Class MyList that inherits from list"
    def print_sorted(self):
        sor = sorted(self)
        print(sor)
