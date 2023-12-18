#!/usr/bin/python3

def magic_calculation(a, b):
    the_resultt = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                the_result += a ** b / i
        except Exception:
            the_result = b + a
            break
    return the_result
