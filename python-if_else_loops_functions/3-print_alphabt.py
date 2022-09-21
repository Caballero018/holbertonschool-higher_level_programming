#!/usr/bin/python3
i = 97
while i <= 122:
    if not (i == 101 or i == 113):
        print("{}" .format(chr(i)), end="")        
    i += 1
print("")
