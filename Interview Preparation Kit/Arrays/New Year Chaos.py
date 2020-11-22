#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q = [P-1 for P in q]
    step = 0
    for i, P in enumerate(q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1, 0), i):
            if q[j] > P:
                step += 1
    print(step)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

########################################
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    step = 0
    for i in range(len(q)):
        if q[i] -(i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(q[i]-2,0), i):
            if q[j] > q[i]:
                step += 1
    print(step)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
