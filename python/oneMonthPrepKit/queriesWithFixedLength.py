#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    result = []
    for query in queries:
        maxNum = max(arr[:query])
        minNum = maxNum

        for i in range(d, len(arr)):
            if arr[i-d] == maxNum:
                maxNum = max(arr[i-d+1:i+1])
            elif arr[i] > maxNum:
                maxNum = arr[i]
            if maxNum < minNum:
                minNum = maxNum
        result.append(minNum)

    return result



if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
