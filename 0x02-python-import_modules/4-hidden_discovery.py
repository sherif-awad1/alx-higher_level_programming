#!/usr/bin/python3
'''
File: 4-hidden_discovery.py

Author: Sherif Awad
'''


if __name__ == "__main__":
    ''' print all in hidden file '''
    import hidden_4

    nms = dir(hidden_4)
    for name in nms:
        if name[:2] != "__":
            print(name)

