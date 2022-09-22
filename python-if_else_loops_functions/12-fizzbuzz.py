#!/usr/bin/python3
def fizzbuzz():
    n = 1
    while n <= 100:
        if not ((n % 3 == 0) or (n % 5 == 0) or (n % 15 == 0)):
            print(n, end=" ")
        if n % 3 == 0 and not (n % 5 == 0):
            print("Fizz", end=" ")
        if n % 5 == 0 and not (n % 3 == 0):
            print("Buzz", end=" ")
        if (n % 15 == 0):
            print("FizzBuzz", end=" ")
        n += 1
