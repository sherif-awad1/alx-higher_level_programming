#!/usr/bin/python3
# Author: Sherif Awad

def safe_print_division(a, b):
    """print division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
