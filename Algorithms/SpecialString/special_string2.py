#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    prev = ''
    count = 0
    total_count = 0

    for i, v in enumerate(s):
        count += 1

        if i and (v != prev):

            j = 1
            while (i - j >= 0) and (i + j < n) and (j <= count):
                if (s[i - j] == prev) and (s[i + j] == prev):
                    total_count += 1
                    j += 1
                else:
                    break

            count = 1

        total_count += count
        prev = v

    return total_count


if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
