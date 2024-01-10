#!/usr/bin/python3
"""
File: 5-number_keys.py

Author: Sherif Awad
"""


def number_keys(a_dictionary):
    '''function that returns the number of keys in a dictionary'''
    num = 0
    list_keys = list(a_dictionary.keys())
    for i in list_keys:
        num += 1
    return (num)
