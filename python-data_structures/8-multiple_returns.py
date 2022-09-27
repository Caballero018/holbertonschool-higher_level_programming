#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    if not (sentence == ""):
        tup = (len(sentence), sentence[0])
        return tup
    else:
        sentence = None
        tup = (0, sentence)
        return tup
