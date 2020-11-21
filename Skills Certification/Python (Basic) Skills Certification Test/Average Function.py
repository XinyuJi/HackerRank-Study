#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) > 1:
        return(float(sum(nums))/float(len(nums)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
