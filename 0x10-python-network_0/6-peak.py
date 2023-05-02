#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(my_list=[]):
    """ function that finds a peak in a list of unsorted integers."""
    max = None
    if my_list != []:
        max = my_list[0]
        for num in my_list:
            if num > max:
                max = num
    return max
