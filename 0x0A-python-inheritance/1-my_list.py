#!/usr/bin/python3
# Author: Sherif Awad
"""Defines an inherited list class MyList."""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
