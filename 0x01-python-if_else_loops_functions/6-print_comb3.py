#!/usr/bin/python3
i = 0
j = 1
while i <= 7:
    while j <= 9:
        print("{}{}".format(i, j), end=", ")
        j = j + 1
    i = i + 1
    j = i + 1
print("{}{}".format(i, j))
