#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    biggestValueSoFar = [arr[0]]
    for i in range(1, len(arr)):
        biggestValueSoFar.append(max(arr[i], arr[i]+biggestValueSoFar[i-1]))
    
    maxValue = max(biggestValueSoFar)
    
    subsequenceMax = 0
    for value in arr:
        if value >0:
            subsequenceMax+=value
            
    if subsequenceMax <=0:
        subsequenceMax = maxValue
    return [maxValue, subsequenceMax]
        
if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
