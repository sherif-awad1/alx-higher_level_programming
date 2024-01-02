#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#chack if negativ
if (number < 0):
    print(f"{number:d} is negative")
#check if zero
elif (number == 0):
    print(f"{number:d} is zero")
#chak if postive
elif (number > 0):
    print(f"{number:d} is positive")
