#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    mt = []
    for i in range(len(matrix)):
        mat = []
        for j in range(len(matrix[0])):
            if not (isinstance(matrix[i][j], int) or isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            mat.append(round(matrix[i][j] / div, 2))
        if j != len(matrix[0]) - 1:
            raise TypeError("Each row of the matrix must have the same size")
        mt.append(mat)
    return mt 
