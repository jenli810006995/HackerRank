#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# Use slicing

def rotLeft(a, d):
    # arr - array to rotate
    # n - n number of rotations
    # For number of rotations greater than length of array
    d = d % len(a)
    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
