#!/usr/bin/python3
'''
File: 102-magic_calculation.py

Author: Sherif Awad
'''


def magic_calculation(a, b, c):
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
