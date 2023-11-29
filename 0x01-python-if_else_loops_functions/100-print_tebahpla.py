#!/usr/bin/python3
# Goodluck N. TIMOTHY, @southboy_tim on SM

#Print the alphabet in reverse order alternating upper/lower-case

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
