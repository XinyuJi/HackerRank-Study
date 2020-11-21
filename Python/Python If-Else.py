#!/bin/python3

import math
import os
import random
import re
import sys


def weirdornot(n):
    if n%2!=0:
        print('Weird')
        return
    else:
        if n >=2 and n<=5 and n >20:
            print('Not Weird')
            return
        elif n>=6 and n<=20:
            print('Weird')
            return
        else:
            print('Not Weird')
            return

if __name__ == '__main__':
    n = int(input().strip())
    weirdornot(n)
