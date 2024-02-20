#!/usr/bin/python3
# Author: Sherif Awad
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        safe = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return safe
