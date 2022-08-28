#!/usr/bin/python3
def no_c(my_string):
    charr = ""
    i = 0
    for char in my_string:
        if ord(char) == ord('c') or ord(char) == ord('C'):
            char = ""
        charr = charr + char
    return charr
