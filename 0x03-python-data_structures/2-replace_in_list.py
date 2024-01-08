#!/usr/bin/python3
'''
File: 2-replace_in_list.py
Author: Sherif Awad
'''


def replace_in_list(my_list, idx, element):
    ''' replaces an element of a list at a specific position (like in C) '''
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
