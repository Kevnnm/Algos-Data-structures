#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    contests.sort(key=lambda contests: contests[1])
    total = 0
    important = []
    for i, val in enumerate(contests):
        total += val[0]

        if val[1] == 0:
            continue

        important.append(val[0])

    important.sort()
    print(important, k)
    s = 0
    minus = min(len(important), k)
    for i in range(len(important) - minus):
        print(important[i])
        s += important[i]

    print(s)
    return total - s * 2


if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()


