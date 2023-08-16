#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    list(map(lambda num: new_set.add(num), my_list))
    result = sum(new_set)
    return result
