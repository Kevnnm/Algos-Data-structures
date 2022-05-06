#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild2(s1, s2):
    prev = [0] * (len(s2) + 1)
    curr = [0] * (len(s2) + 1)

    for r in s1:
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j - 1] + 1 if r == c else max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return prev[-1]


def commonChild(s1, s2):
    m, n = len(s1), len(s2)
    prev, cur = [0] * (n + 1), [0] * (n + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cur[j] = 1 + prev[j - 1]
            else:
                cur[j] = max(cur[j - 1], prev[j])
        cur, prev = prev, cur
    return prev[n]


if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
