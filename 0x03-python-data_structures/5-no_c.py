#!/usr/bin/python3
'''
File: 5-no_c.py
Author: Sherif Awad
'''


def no_c(my_string):
    '''removes all characters c and C from a string'''
    new = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(new))
