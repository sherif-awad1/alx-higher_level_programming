#!/usr/bin/python3
# Author: Sherif Awad

class MyInt(int):
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
