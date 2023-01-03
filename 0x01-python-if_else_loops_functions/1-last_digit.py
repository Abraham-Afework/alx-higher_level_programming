#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    neg = "-"
else:
    neg = ""

number = str(number)
last = int(neg + number[-1])

if last < 6 and last != 0:
    print(f"Last digit of {number} is {neg}{number[-1]}", end=" ")
    print("and is less than 6 and not 0")
elif last > 5:
    print(f"Last digit of {number} is {neg}{number[-1]} and is greater than 5")
else:
    print(f"Last digit of {number} is {number[-1]} and is 0")
