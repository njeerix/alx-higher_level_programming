#!/usr/bin/python3

"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """Class Square that defines a squre with a private size attribute."""

    def __init__(self, size):
        """Instantiation with a given size (no type/value verification)."""
        self.__size = size
