#!/usr/bin/python3
def new_in_list(my_list, idx, new_element) :
   
       if idx > 0 and idx < len(my_list):
             new_list = my_list[0:]
             new_list.pop(idx)
             new_list.insert(idx,9)
             return new_list
       else:
             return None
