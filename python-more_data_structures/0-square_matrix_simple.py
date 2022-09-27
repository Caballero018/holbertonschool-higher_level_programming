#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in range(len(matrix)):
        matr = []
        for j in range(len(matrix[0])):
            matr.append(matrix[i][j] ** 2)
        mat.append(matr)
    return mat
