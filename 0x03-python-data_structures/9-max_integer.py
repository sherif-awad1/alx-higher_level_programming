#!/usr/bin/python3
'''
File: 9-max_integer.py
Author: Sherif Awad
'''


def max_integer(my_list=[]):
    ''' '''
    if len(my_list) == 0:
        return (None)

    mex = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > mex:
            mex = my_list[i]
    return (mex)
