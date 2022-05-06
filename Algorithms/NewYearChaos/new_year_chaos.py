#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    chaotic = False
    count = 0

    for i in range(len(q)):
        actual_label = q[i]

        if i < actual_label - 3:
            print("Too chaotic")
            chaotic = True
            break

        # Look for correct value
        far_left = max(actual_label - 2, 0)
        for i2 in range(far_left, i + 1):
            if q[i2] and q[i2] > actual_label:
                count += 1

    if not chaotic:
        print(count)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
