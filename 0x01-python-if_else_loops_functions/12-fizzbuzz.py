#!/usr/bin/python3
def fizzbuzz():

    num = ""

    for i in range(1, 101):

        if i % 3 == 0 and i % 5 != 0:
            num = "Fizz"
        elif i % 5 == 0 and i % 3 != 0:
            num = "Buzz"
        elif i % 3 == 0 and i % 5 == 0:
            num = "FizzBuzz"
        else:
            num = str(i)
        print("{}".format(num), end=" ")
