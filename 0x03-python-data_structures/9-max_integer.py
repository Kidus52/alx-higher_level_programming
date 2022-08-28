#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)
    if leng == 0:
        return None
    else:
        maxm = my_list[0]
        for i in my_list:
            if i >= maxm:
                maxm = i
        return maxm
