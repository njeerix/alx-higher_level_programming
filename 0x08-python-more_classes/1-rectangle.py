#!/usr/bin/python3
"""This module contains the Rectangle class."""


class Rectangle:
    """A class to represent a rectangle."""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def get_width(self):
        return self.__width
    
    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
