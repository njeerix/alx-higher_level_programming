#!/usr/bin/python3
def add_integer(a, b=None):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if b is not None and not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if b is None:
        b = 98
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
