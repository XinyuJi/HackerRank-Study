#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dictionary = {}
    res = 0
    for i in ar:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    for i in dictionary.values():
        if i > 1:
            res += i//2
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
