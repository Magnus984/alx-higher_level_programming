#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        numElements = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            numElements += 1
        print()
        return numElements
    except Exception:
        print()
        return numElements
