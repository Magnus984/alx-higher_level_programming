#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    list_of_operators = ["+", "-", "*", "/"]
    result = 0
    if (len(argv) - 1) != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    if argv[2] not in list_of_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argv[2] == "+":
        result = add(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] == "-":
        result = sub(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] == "*":
        result = mul(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] == "/":
        result = div(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
