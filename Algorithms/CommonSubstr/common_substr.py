#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    d1 = {}

    for char in s1:
        d1[char] = True

    for char in s2:
        if char in d1:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
