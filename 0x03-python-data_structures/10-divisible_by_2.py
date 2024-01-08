#!/usr/bin/python3
'''
File: 10-divisible_by_2.py
Author: Sherif Awad
'''


def divisible_by_2(my_list=[]):
    ''' function that finds all multiples of 2 in a list. '''
    copy_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            copy_list.append(True)
        else:
            copy_list.append(False)
    return copy_list
