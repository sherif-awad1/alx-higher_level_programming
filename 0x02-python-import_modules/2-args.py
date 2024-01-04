#!/usr/bin/python3
'''
File: 2-args.py

Author: Sherif Awad
'''


if __name__ == "__main__":
    ''' print count argments list'''
    import sys

    leng = len(sys.argv) - 1
    if leng == 1:
        print("1 argument:")
    else:
        print("{} arguments".format(leng))
    for n in range(leng):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
