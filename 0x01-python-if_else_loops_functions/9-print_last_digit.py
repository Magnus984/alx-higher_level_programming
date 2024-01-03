#!/usr/bin/python3
def print_last_digit(number):
    mod_num = 1
    if number < 0:
        mod_num = -1 * number
        last_digit = mod_num % 10
    else:
        last_digit = number % 10
    print(f"{last_digit}", end='')
    return last_digit
