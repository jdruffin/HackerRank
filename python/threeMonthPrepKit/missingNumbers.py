#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    counterA = Counter(arr)
    counterB = Counter(brr)
    returnArray = []
    for key in counterB:
        if key not in counterA:
            returnArray.append(key)
        elif counterB[key] > counterA[key]:
            returnArray.append(key)

    returnArray.sort()
    return returnArray

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
