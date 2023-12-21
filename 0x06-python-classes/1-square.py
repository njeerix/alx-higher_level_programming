#!/usr/bin/python3

class Square:
    """Class Square that defines a squre with a private size attribute."""

    def __init__(self, size):
        """Instantiation with a given size (no type/value verification)."""
        self.__size = size

mysquare = Square(3)
print(f"<class '1-square.Square'>")
print(f"{{'_Square__size': {mysquare._Square__size}}}")

mysquare = Square(89)
print(f"<clas '1-square.Square'>")
print(f"{{'_Square__size': {mysquare._Square__size}}}")

try:
    print(mysquare._Square__size)
except AttributeError as e:
    print(e)
