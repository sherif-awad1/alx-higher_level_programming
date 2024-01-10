#!/usr/bin/python3
"""
File: 102-complex_delete.py

Author: Sherif Awad
"""


def complex_delete(a_dictionary, value):
    '''function that deletes keys with a specific value in a dictionary'''
    list_of_key = list(a_dictionary.keys())
    for i in list_of_key:
        if value == a_dictionary.get(i):
            del a_dictionary[i]
    return (a_dictionary)
