#!/usr/bin/python3
'''
File:6-print_matrix_integer.py
Author: Sherif Awad
'''


def print_matrix_integer(matrix=[[]]):
    ''' function that prints a matrix of integers. '''
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" " if j != i[-1] else "")
        print("")
