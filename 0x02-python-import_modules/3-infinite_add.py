#!/usr/bin/python3
'''
File: 3-infinite_add.py

Author: Sherif Awad
'''


if __name__ == "__main__":
    ''' print sum of all argment '''
    import sys

    count = 0
    leng = len(sys.argv) - 1
    for n in range(leng):
        count += int(sys.argv[n + 1])
    print("{}".format(count))
