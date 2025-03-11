#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    array = [0 for i in range(n+2)]

    for query in queries:
        start, end, value = query
        array[start] += value
        array[end+1] -= value

    runningTotal = 0
    runningMax = 0
    for value in array:
        runningTotal += value
        runningMax = max(runningMax, runningTotal)

    return runningMax


if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
