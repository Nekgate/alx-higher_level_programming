#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    Replace all occurences of an element by another in a new list.
    '''
    return [replace if num == search else num for num in my_list]
