#!/usr/bin/python3
'''
File: 4-new_in_list.py
Author: Sherif Awad
'''


def new_in_list(my_list, idx, element):
    '''  replaces element in list at position '''
    copy = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
