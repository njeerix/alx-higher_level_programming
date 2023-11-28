#!/usr/bin/python3
alphabet = ""
for letter in range(ord('a'), ord('z') + 1):
    alphabet += "{}".format(chr(letter))
print(alphabet, end="")
