#!/usr/bin/python3
'''
File: 3-print_alpha.py
Author: Sherif Awad
'''
for alpha in range(97, 123):
    if chr(alpha) != 'e' and chr(alpha) != 'q':
        print("{}".format(chr(alpha)), end="")
