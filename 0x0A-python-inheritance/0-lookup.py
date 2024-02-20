#!/usr/bin/python3
# Author: Sherif Awad
"""def object attribute lookup function"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
