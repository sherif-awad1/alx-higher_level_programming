#!/usr/bin/python3
# from_json_string.py
# aUTHOR: Sherif Awad

"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
