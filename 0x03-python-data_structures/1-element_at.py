#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx not in range(len(my_list)):
        return None
    else:
        return my_list[idx]
