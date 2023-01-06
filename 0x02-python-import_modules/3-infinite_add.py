#!/usr/bin/python3
import sys
if __name__ == "__main__":
    addition = sys.argv[1:]
    sum = 0
    for i in range(len(addition)):
        sum = sum + int(addition[i])
    print("{}".format(sum))
