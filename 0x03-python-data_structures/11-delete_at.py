#!/usr/bin/python3
'''
File: 11-delete_at.py
Author: Sherif awad
'''


def delete_at(my_list=[], idx=0):
    ''' function that deletes item at specific position in list '''
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
    return my_list
