#!/usr/bin/python3
'''
File: 7-islower.py
Author: Sherif Awad
'''

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
