#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    res = 0
    point = -1
    count = 0
    for i in range(len(path)):
        if path[i] == "D":
            res -= 1
            if res == -1:
                point = i
        else:
            res += 1
            if res == 0 and point != -1 and i > point:
                count += 1
                point = -1
    if point != -1:
        count += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
