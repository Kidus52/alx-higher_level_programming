#!/usr/bin/python3
i = 1
char = ord("z")
while char >= ord("a"):
    if i % 2 == 0:
        char = char - 32
    print("{}".format(chr(char)), end="")
    if i % 2 == 0:
        char = char + 32
    i = i + 1
    char = char - 1
