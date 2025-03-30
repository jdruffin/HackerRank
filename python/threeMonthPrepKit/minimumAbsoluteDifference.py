#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()

    minAbsDiff = 2000000000
    for i in range(1, len(arr)):
        absDiff = arr[i] - arr[i-1] 
        if absDiff < minAbsDiff:
            minAbsDiff = absDiff

    return minAbsDiff 
if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
