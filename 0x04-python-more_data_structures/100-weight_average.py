#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weight_sum = 0
    num = 0
    for i in range(len(my_list)):
        weight_sum += my_list[i][1]
    for i in range(len(my_list)):
        num += (my_list[i][0] * my_list[i][1])
    average = num / weight_sum
    return average
