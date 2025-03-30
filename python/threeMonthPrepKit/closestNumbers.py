#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here

    arr.sort()
    minDistance = 200000000
    for i in range(1,len(arr)):
        difference = arr[i] - arr[i-1]
        if difference < minDistance:
            minDistance = difference

    returnArray = []
    for i in range(1,len(arr)):
        difference = arr[i] - arr[i-1]
        if difference == minDistance:
            returnArray.append(arr[i-1])
            returnArray.append(arr[i])

    return returnArray


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
