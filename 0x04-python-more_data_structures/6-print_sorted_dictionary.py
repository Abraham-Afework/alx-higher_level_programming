#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_count = sorted(a_dictionary)
    for idx in key_count:
        print("{}: {}".format(idx, a_dictionary[idx]))
