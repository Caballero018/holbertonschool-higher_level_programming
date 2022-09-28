#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and a_dictionary != {}:
        max_key = max(a_dictionary, key=lambda key: a_dictionary[key])
        return max_key
