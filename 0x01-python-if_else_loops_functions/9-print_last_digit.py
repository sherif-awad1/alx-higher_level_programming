#!/usr/bin/python3
'''
File: print_lats_digit.py
Author: Sherif Awad
'''


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
