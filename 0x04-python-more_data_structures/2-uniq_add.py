#!/usr/bin/python3
"""
File: 2-uniq_add.py

Author: Sherif Awad
"""


def uniq_add(my_list=[]):
    """function that adds all unique integers in a list"""
    create = 0
    for ig in set(my_list):
        create += ig
    return (create)
