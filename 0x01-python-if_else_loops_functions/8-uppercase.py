#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        ascii_value = ord(char)
        uppercase_char = char if not (97 <= ascii_value <= 122) else chr(ascii_value - 32)
        print("{}".format(uppercase_char), end="")
    print()
