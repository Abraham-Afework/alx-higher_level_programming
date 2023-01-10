#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        
    for i in matrix:
       for y in i:
            print("{}".format(y), end="")
            
            if y != i[-1]:
                print(end=" ")   
       print()