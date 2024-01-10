#!/usr/bin/python3
"""
File: 8-simple_delete.py

Author: Sherif Awad
"""


def simple_delete(a_dictionary, key=""):
    '''function that deletes a key in a dictionary'''
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
