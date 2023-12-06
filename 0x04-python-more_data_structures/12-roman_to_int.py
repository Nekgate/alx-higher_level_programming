#!/usr/bin/python3

def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) != str):
        return 0
    roman = 0
    num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    limit = len(roman_string)
    for i in range(0, limit):
        if i == len(roman_string) - 1:
            roman += num[roman_string[i]]
        elif num[roman_string[i]] >= num[roman_string[i + 1]]:
            roman += num[roman_string[i]]
        else:
            roman -= num[roman_string[i]]
    return roman
