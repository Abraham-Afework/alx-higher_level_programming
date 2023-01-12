#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary:
        max = list(a_dictionary.values())[0]
        big_key = ""
        for key, val in a_dictionary.items():
            if max <= val:
                max = val
                big_key = key
        return big_key
    else:
        return None
