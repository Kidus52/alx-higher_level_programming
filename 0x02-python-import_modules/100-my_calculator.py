#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    num_of_arg = len(argv[1:])
    if num_of_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i, arg in enumerate(argv[1:]):
        if i == 0:
            arg1 = int(arg)
        elif i == 1:
            arg2 = arg
        elif i == 2:
            arg3 = int(arg)
    if arg2 == '+':
        value = add(arg1, arg3)
    elif arg2 == '-':
        value = sub(arg1, arg3)
    elif arg2 == '*':
        value = mul(arg1, arg3)
    elif arg2 == '/':
        value = div(arg1, arg3)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(arg1, arg2, arg3, value))
    exit(0)
