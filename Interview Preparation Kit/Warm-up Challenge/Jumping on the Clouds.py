#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    point = 0
    while point < (len(c)-2):
        if c[point+2] == 0:
            jump += 1
            point += 2
        else:
            point += 1
            jump += 1
    if point == len(c) - 2:
        jump += 1
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
