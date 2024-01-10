#!/usr/bin/python3
"""
File: 10-best_score.py

Author: Sherif Awad
"""


def best_score(a_dictionary):
    """function that returns a key with the biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    dif = list(a_dictionary.keys())[0]
    pt = a_dictionary[dif]
    for k, v in a_dictionary.items():
        if v > pt:
            pt = v
            dif = k
    return (dif)
