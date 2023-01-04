#!/usr/bin/python3
start = ord('z')
end = ord('a')
for text in range(start, end-1, -1):
    if text % 2 != 0:
        print(chr(text).upper(), end="")
    else:
        print(chr(text), end="")
