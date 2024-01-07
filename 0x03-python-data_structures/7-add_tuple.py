#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        tuple_res = (0, 0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        result_zero_index = tuple_a[0] + tuple_b[0]
        result_one_index = 0
        tuple_res = (result_zero_index, result_one_index)
    elif len(tuple_a) == 0:
        result_zero_index = tuple_b[0]
        result_one_index = tuple_b[0]
        tuple_res = (result_zero_index, result_one_index)
    elif len(tuple_a) == 1:
        result_zero_index = tuple_a[0] + tuple_b[0]
        result_one_index = 0 + tuple_b[1]
        tuple_res = (result_zero_index, result_one_index)
    elif len(tuple_b) == 0:
        result_zero_index = tuple_a[0]
        result_one_index = tuple_a[0]
        tuple_res = (result_zero_index, result_one_index)
    elif len(tuple_b) == 1:
        result_zero_index = tuple_a[0] + tuple_b[0]
        result_one_index = tuple_a[0]
        tuple_res = (result_zero_index, result_one_index)
    else:
        result_zero_index = tuple_a[0] + tuple_b[0]
        result_one_index = tuple_a[1] + tuple_b[1]
        tuple_res = (result_zero_index, result_one_index)
    return tuple_res
