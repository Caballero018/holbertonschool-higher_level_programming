#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = -1 * ((-1 * number) % 10)
        return last
    n = number % 10
    return n

        
    