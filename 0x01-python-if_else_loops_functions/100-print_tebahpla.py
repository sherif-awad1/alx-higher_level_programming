#!/usr/bin/python3
'''
File: 100-print_tevapl.py

Author: Sherif Awad
'''


i = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print('{}'.format(chr(ch - i)), end="")
    i = 32 if i == 0 else 0

