#!/usr/bin/python3
# Author: Sherif Awad
"""def class-checking fun"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
