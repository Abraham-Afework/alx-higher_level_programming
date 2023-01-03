#!/usr/bin/python3
def print_last_digit(number):
    if type(number) == int:
        number = str(number)
        number = number[-1]
        print("{}".format(number), end="")
        return number
    else:
        raise Exception('error please enter a number')
