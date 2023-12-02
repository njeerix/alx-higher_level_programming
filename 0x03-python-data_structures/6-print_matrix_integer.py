#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_index, element in enumerate(row):
            if col_index == len(row) - 1:
                print("{:d}".format(element))
            else:
                print("{:d}".format(element), end=" ")
    if not matrix:
        print()
