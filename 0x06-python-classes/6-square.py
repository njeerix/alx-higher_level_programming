#!/usr/bin/python3

"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """Class Square that defines a square with private size attribute."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiation with an optical size and position.

        Args:
            size (int): Size of the square (default is 0).
                Must be an integer, otherwise raise a TypeError exception.
                If size is less than 0, raise a ValueError exception.
            posistion (tuple): Position of the square (default is (0, 0)).
                Must be a tuple of 2 positive integers, otherwisw raise a TypeError exception.

        Returns:
            None
        """
        self.size = size
        self.position = position

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
        Setter method to set the size.

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

    @property
    def position(self):
        """
        Getter method to retrieve the position.

        Returns:
            tuple: Position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position.

        Args:
            value (tuple): New position value.

        Raises:
            TypeError: If position is not tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 postive integers")
        else:
            self.__position = value

    def area(self):
        """
        Public instance method to calculate the area of the square.

        Args:
            None

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method to print the square using the character # and using the position.

        Args:
            None

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
