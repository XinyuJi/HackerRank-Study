#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if s == "a":
        return n
    count = n//len(s) * s.count("a")
    rest = n % len(s)
    if rest != 0:
        for i in range(rest):
            if s[i] == "a":
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
