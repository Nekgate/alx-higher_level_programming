#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    dnums = 0
    for i in range(dnums, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            dnums += 1
        except (ValueError, TypeError):
            pass
    print()
    return dnums
