#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
last_digit = number % 10

if number > 0:
	if last_digit > 5:
		print(f"Last digit of {number} is {last_digit} and is greater than 5")
	elif last_digit == 0:
		print(f"Last digit of 0 is {last_digit} and is 0")
	elif last_digit < 6:
		print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
if number < 0:
	if last_digit > 5:
		print(f"Last digit of {number} is -{n[-1:]} and is greater than 5")
	elif last_digit == 0:
		print(f"Last digit of 0 is {last_digit} and is 0")
	elif last_digit < 6:
		print(f"Last digit of {number} is -{n[-1:]} and is less than 6 and not 0")




