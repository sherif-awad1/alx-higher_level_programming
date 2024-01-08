#!/usr/bin/python3
'''
File: 3-print_reversed_list_integer.py
Author: Sherif Awad
'''


def print_reversed_list_integer(my_list=[]):
    '''prints all integers of a list, in reverse orde '''
    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
