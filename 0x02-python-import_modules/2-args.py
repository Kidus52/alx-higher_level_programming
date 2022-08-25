#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_of_arg = len(argv[1:])
    if num_of_arg == 0:
        print("{:d} arguments.".format(num_of_arg))
    else:
        if num_of_arg == 1:
            print("{:d} argument:".format(num_of_arg))
        else:
            print("{:d} arguments:".format(num_of_arg))
        for i, arg in enumerate(argv[1:]):
            print("{:d}: {:s}".format(i + 1, arg))
