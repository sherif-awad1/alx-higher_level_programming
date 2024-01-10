#!/usr/bin/python3
"""
File: 4-only_diff_elements.py

Author: Sherif Awad
"""


def only_diff_elements(set_1, set_2):
    """ function that returns a set of all elements present in only one"""
    return (set_1 ^ set_2)
