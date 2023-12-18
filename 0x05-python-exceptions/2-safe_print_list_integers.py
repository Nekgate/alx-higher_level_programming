#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(x):
            value = int(my_list[i])
            print("{:d}".format(value), end=" ")
            cnt += 1 
    except (ValueError, IndexError):
        pass
    print()
    return cnt
