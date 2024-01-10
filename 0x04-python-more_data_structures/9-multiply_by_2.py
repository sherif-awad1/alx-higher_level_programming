#!/usr/bin/python3
"""
File: 9-multiply_by_2.py

Author: Sherif Awad
"""


def multiply_by_2(a_dictionary):
    ndir = a_dictionary.copy()
    list_dir = list(ndir.keys())
    for i in list_dir:
        ndir[i] *= 2
    return (ndir)
