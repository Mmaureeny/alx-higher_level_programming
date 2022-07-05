#!/usr/bin/python3
"""Module 0-lookup.
Defines an object attribute lookup function.
"""


def lookup(obj):
    """Returns that list of attributes and methods.
    Args:
        - obj: object to look into
    """

    return dir(obj)
