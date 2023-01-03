#!/usr/bin/python3
def uppercase(str):
    text = ""
    for c in str:
        if ord(c) in range(97, 123):
            c = ord(c) - 32
        else:
            c = ord(c)
        text += chr(c)
    print("{}".format(text))
