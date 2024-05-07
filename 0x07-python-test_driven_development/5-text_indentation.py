#!/usr/bin/python3

"""
This module contains a function to print text with 2 new linew after characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':' character.
    Parameters:
        text (str): The Input text.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    for char in text:
        print(char, end="")
        if char in separators:
            print("\n\n", end="")
