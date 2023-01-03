#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        zero = "0"
    else:
        zero = ""
    if i != 99:
        print("{}{}".format(zero, i), end=", ")
    else:
        print("{}".format(i))
