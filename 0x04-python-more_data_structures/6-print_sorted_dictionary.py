#!/usr/bin/python3
"""
File: 6-print_sorted_dictionary.py

Author: Sherif Awad
"""


def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys"""
    [print("{}: {}".format(d, a_dictionary[d])) for d in sorted(a_dictionary)]
