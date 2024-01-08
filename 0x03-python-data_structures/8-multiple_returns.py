#!/usr/bin/python3
'''
File: 8-multiple_returns.py
Author: Sherif Awad
'''


def multiple_returns(sentence):
    '''function that returns a tuple with the length of a string'''
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
