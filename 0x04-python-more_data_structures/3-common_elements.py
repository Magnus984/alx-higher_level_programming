#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for element1 in set_1:
        for element2 in set_2:
            if element1 == element2:
                common_set.add(element1)
    return common_set
