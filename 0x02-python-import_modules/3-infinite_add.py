#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_of_arg = len(argv[1:])
    Sum = 0
    if num_of_arg == 0:
        print("{:d}".format(num_of_arg))
    else:
        for i, arg in enumerate(argv[1:]):
            Sum += int(arg)
        print("{:d}".format(Sum))
