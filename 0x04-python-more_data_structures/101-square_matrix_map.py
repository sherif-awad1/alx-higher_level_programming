#!/usr/bin/python3
"""
File: 101-square_matrix_map.py

Author: Sherif Awad
"""


def square_matrix_map(matrix=[]):
    ''' function that computes the square value of all integers'''
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
