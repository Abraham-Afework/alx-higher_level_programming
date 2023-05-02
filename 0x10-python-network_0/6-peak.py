#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""
def find_peak(my_list=[]):
    max = None
    if my_list != []:
        max = my_list[0]
        for num in my_list:
            if num > max:
                max = num
    return max


