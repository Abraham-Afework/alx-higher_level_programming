#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
        except Exception as err:
            return err
    print()
    return (count)
