def safe_print_list_integers(my_list=[], x=0):
    try:
        numElements = 0
        for i in range(x):
            if not (isinstance(my_list[i], int)):
                continue
            else:
                print("{:d}".format(my_list[i]), end="")
                numElements += 1
        print()
        return numElements
    except ValueError:
        print()
        return numElements
