#!/usr/bin/python3
"""
File: 11-multiply_list_map.py

Author: Sherif Awad
"""


def multiply_list_map(my_list=[], number=0):
    '''function that returns a list with all values multiplied '''
    return (list(map((lambda i: i * number), my_list)))
