#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = [list(map(lambda x: x * x, row)) for row in matrix]
    return new_matrix
