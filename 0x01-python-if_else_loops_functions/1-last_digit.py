#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last = int(number[-1])

if last < 6 and last != 0:
    print(f"Last digit of {number} is {number[-1]}", end=" ")
    print("and is less than 6 and not 0")
elif last > 5:
    print(f"Last digit of {number} is {number[-1]} and is greater than 5")
else:
    print(f"Last digit of {number} is {number[-1]} is 0 and 0")
