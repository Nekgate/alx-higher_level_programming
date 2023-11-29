#!/usr/bin/python3
# Goodluck N. Timothy <@southboy_tim on SM>


# This function creates a copy of the string without the character at position n.
def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
