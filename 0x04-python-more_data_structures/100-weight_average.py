#!/usr/bin/python3
"""
File: 100-weight_average.py

Author: Sherif Awad
"""


def weight_average(my_list=[]):
    ''' function that returns the weighted average of all integers'''
    if not my_list:
        return 0
    count = 0
    men = 0
    for i in my_list:
        count += i[0] * i[1]
        men += i[1]
    return (count / men)
