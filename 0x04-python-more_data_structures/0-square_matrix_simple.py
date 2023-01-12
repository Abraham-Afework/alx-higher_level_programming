#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    if matrix:
        for i in matrix:
            single = []
            for j in i:
                single.append(j**2)
            new.append(single)
    return new
