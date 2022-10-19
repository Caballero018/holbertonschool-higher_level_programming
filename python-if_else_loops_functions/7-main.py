#!/usr/bin/python3
islower = __import__('7-islower').islower

print("'' => {}".format("lower" if islower("") else "upper"))