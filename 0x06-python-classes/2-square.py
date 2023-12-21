#!/usr/bin/python3

"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """Class Square that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Instantiation with an optical size.


        Args:
            size (int): Size of the square (default is 0).
                Must be an integer, otherwise raise a TypeError exception.
                If size is less than 0, raise a ValueError exception.

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
