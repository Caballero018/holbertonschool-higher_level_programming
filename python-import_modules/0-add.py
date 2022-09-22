#!/usr/bin/python3
if __name__ == "__main__":
    ad = __import__('add_0').add
    a = 1
    b = 2
    print("1 + 2 = {}" .format(ad(a, b)))