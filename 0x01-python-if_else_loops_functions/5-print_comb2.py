#!/usr/bin/python3
'''
File: 5-print_comb2.py
Author: Sherif Awad
'''
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
