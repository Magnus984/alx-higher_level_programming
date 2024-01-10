#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mod_list = my_list[:]
    for i in range(len(mod_list)):
        if mod_list[i] == search:
            mod_list[i] = replace
    return mod_list
