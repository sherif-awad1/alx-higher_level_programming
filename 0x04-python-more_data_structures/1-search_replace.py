#!/usr/bin/python3
"""
File: 1-search_replace.py

Author: Sherif Awad
"""


def search_replace(my_list, search, replace):
    ''' function that replaces all occurrences of an element'''
    rep_list = list(map(lambda x: replace if x == search else x, my_list))
    return (rep_list)
