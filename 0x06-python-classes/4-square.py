#!/usr/bin/python3

"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """Class Square that defines a square with private size attribute."""

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
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Seeter method to set the size.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method to calculate the area of the square.

        Args:
            None

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2
