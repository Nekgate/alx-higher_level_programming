#!/usr/bin/python3
def no_c(my_string):
    listchars = list(my_string)
    for char in listchars:
        if char == 'c' or char == 'C':
            listchars.remove(char)
    return("".join(listchars))
