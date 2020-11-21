#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    k = d % len(a)
    if k == 0:
        return a
    
    if d < len(a):
        while d > 0:
            a.append(a[0])
            a.pop(0)
            d = d - 1
        return a
    
    elif d > len(a):
        while k > 0:
            a.append(a[0])
            a.pop(0)
            k = k - 1
        return a
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
