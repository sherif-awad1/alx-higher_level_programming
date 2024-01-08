#!/usr/bin/python3
'''
File:0-print_list_integer.py
Author: Sherif Awad
'''


def print_list_integer(my_list=[]):
    ''' print integer listtt '''
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
