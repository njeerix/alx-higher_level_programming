#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for i in range(x):
            if i < len(my_list):
                if type(my_list[i]) == int:
                    print("{:d}".format(my_list[i]), end="")
                    printed_integers += 1
            else:
                raise IndexError("list index out of range")
    except IndexError as e:
        print(e)
    finally:
        print()
        return printed_integers
