#!/usr/bin/python3
"""
File: 11-multiply_list_map.py

Author: Sherif Awad
"""


def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda c: c*number), my_list)))
