#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = sorted(a_dictionary.values())
    for key in a_dictionary:
        if val[-1] == a_dictionary[key]:
            return key
