#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    previous_length = 0
    previous_char = s[0]
    total_count = 0

    for i, char in enumerate(s):
        if i == len(s) - 1:
            if char == previous_char:
                previous_length += 1
                size = 0
                for num in range(previous_length):
                    size += num + 1
                total_count += size
            else:
                size = 0
                for num in range(previous_length):
                    size += num + 1
                total_count += size + 1
        elif char == previous_char:
            previous_length += 1
        elif s[i + 1] == previous_char:
            size = 0
            for num in range(previous_length):
                size += num + 1
            total_count += size

            length = 0
            for index in range(i + 1, len(s)):
                if s[index] != previous_char or length == previous_length:
                    break
                elif s[index] == previous_char:
                    length += 1
            print(length)

            if length == previous_length:
                total_count += previous_length

            previous_char = char
            previous_length = 1
        elif s[i + 1] != previous_char:
            size = 0
            for num in range(previous_length):
                size += num + 1
            total_count += size
            previous_length = 1
            previous_char = char

    return total_count


if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
