#!/usr/bin/python3
""


def pascal_triangle(n):
    ls = []
    if n > 0:
        ls.append([1])
        for r in range(1, n):
            pr = ls[-1]
            ls.append([1] + [pr[i - 1] + pr[i] for i in range(1, r)] + [1])
    return ls
