#!/usr/bin/python3
#file:0-positive_or_negative.py
#author : Sherif Awad

import random
number = random.randint(-10, 10)
''' check if it postive or negtive or 0 '''
if (number < 0):
    print(f"{number:d} is negative")
elif (number == 0):
    print(f"{number:d} is zero")
elif (number > 0):
    print(f"{number:d} is positive")
