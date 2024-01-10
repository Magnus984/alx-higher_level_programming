#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    my_sum = 0
    for integer in my_set:
        my_sum += integer
    return my_sum
