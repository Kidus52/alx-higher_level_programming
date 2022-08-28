#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = 0
    new_list = my_list.copy()
    for i in my_list:
        if (i % 2) == 0:
            new_list[j] = True
        else:
            new_list[j] = False
        j = j + 1
    return new_list
