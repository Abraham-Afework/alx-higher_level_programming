#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if my_list is not None:
        new_list = my_list[0:]
        if idx >= 0 and idx < len(my_list):
            new_list[idx] = new_element
            return new_list
        else:
            return my_list
    else:
        return None
