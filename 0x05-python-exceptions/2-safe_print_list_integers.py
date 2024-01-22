#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numElement = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            numElement += 1;
        except (ValueError, TypeError):
            pass
    print()
    return numElement
