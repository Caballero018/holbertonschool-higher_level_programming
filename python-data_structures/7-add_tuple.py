#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = ()
    tup2 = tuple_a + (0, 0)
    tup3 = tuple_b + (0, 0)
    tup = tup2[0] + tup3[0], tup2[1] + tup3[1]
    return tup
