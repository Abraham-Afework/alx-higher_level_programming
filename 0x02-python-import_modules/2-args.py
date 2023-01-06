#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arg = sys.argv
    arg = arg[1:]

    if len(arg) > 1:
        print("{} arguments:".format(len(arg)))

    elif len(arg) == 0:
        print("{} arguments.".format(len(arg)))
    else:
        print("{} argument:".format(len(arg)))

    for i in range(len(arg)):
        print("{}: {}".format(i+1, arg[i]))
