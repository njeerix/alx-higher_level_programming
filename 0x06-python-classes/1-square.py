#!/usr/bin/python3
class Square:
    """Class Square that defines a squre with a private size attribute."""

    def __init__(self, size):
        """Instantiation with a given size (no type/value verification)."""
        self.__size = size
