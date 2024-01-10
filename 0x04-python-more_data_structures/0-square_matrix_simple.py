#!/usr/bin/python3
"""
File: 0-square_matrix_simple.py

Author: Sherif Awad
"""


def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
