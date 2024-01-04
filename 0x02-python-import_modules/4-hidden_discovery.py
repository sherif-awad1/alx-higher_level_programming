#!/usr/bin/python3
'''
File: 4-hidden_discovery.py

Author: Sherif Awad
'''


if __name__ == "__main__":
    ''' print all in hidden file '''
    import hidden_4

    for n in dir(hidden_4):
        if not n.startswith("__"):
            print("{:s}".format(n))

