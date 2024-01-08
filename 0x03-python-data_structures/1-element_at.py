#!/usr/bin/python3
'''
File:1-element_at.py
Author: Sherif Awad
'''


def element_at(my_list, idx):
    '''retrieves an element from a list like in C '''
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return (my_list[idx])
