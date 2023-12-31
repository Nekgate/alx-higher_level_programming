#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''
    Add up all unique integers in a list (once for each integer).
    '''
    result = 0
    for elem in set(my_list):
        result += elem
    return (result)
