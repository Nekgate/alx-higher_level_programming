#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    t_num = 0
    for i in range(t_num, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            t_num += 1
        except (ValueError, TypeError):
            pass
        print()
        return t_num
