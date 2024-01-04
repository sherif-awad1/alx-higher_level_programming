#!/usr/bin/python3
'''
File: 100-my_caculator.py

Author: Sherif Awad
'''


if __name__ == "__main__":
    '''handle 3arg calalation '''
    from calculator_1 import add, sub, mul, div
    import sys

    leng = len(sys.argv)
    if leng != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    sign = {"+": add, "-":sub, "*":mul, "/":div}
    if op not int sign:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, sign[op](a, b)))
