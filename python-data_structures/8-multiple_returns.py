#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tup = ()
        tup = (len(sentence), sentence[0])
        return tup
    sentence[0] = None
