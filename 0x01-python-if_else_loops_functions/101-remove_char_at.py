#!/usr/bin/python3
'''
File: 101-remove-char at.by

Author: Sherif Awad
'''


def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
