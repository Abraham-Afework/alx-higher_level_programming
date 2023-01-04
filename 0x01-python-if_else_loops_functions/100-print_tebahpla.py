#!/usr/bin/python3
start = ord('z')
end = ord('a')
for text in range(start, end-1, -1):
    if text % 2 != 0:
        alpha = chr(text).upper()
    else:
        alpha = chr(text)
    print("{}".format(alpha), end="")
