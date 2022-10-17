#!/usr/bin/python3
"""Function pascal form"""


def pascal_triangle(n):
    """Function that returns a list of lists of
    integers representing the Pascal’s form of n"""
    form = []
    if n <= 0:
        return form
    elif n == 1:
        form.append([1])
    elif n == 2:
        form.append([1])
        form.append([1, 1])
    else:
        form.append([1])
        form.append([1, 1])
        for i in range(2, n):
            form.append(
                [form[i-1][j-1] + form[i-1][j]
                    if j != 0 and i != j else 1 for j in range(0, i+1)]
            )
    return form
