#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length_of_argv = len(sys.argv)
    if length_of_argv == 1:
        print("{} arguments.".format(length_of_argv - 1))
    elif length_of_argv > 1:
        if length_of_argv == 2:
            print("{} argument:".format(length_of_argv - 1))
        else:
            print("{} arguments:".format(length_of_argv - 1))
        for i in range(1, length_of_argv):
            print("{}: {}".format(i, sys.argv[i]))
