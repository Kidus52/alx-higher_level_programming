#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dic = a_dictionary.copy()
        for key, value in sorted(a_dictionary.items()):
            updating_dic = {key: value * 2}
            new_dic.update(updating_dic)
        return 
