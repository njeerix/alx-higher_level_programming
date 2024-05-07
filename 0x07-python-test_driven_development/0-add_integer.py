#!/usr/bin/python3

"""
This module provides a function to add two integers.
"""


def add_integer(a, b=None):
    """
    Adds two integers.

    Prameters:
       a (int or float): First integer or float.
       b (int or float, optional): Second integer or float.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if b is not None and not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if b is None:
        b = 98
    if isinstance(a, float):
        if a = float('inf') or a == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")
        if a != a:
            raise ValueError("cannot convert float NaN to integer")
        a = int(a)
    if isinstance(b, float):
        if b == float('inf') or b == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")
        if b != b:
            raise ValueError("cannot convert float NaN to integer")
        b = int(b)
    return (a + b)
