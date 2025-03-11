#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr):
    # Write your code here
    cumulativeSums = [0]
    for i in range(1,len(arr)):
        cumulativeSums.append(cumulativeSums[i-1] + arr[i-1])

    reverseCumulativeSums = [0 for i in range(len(arr))]
    for i in range(len(arr)-2,-1, -1):
        reverseCumulativeSums[i] = reverseCumulativeSums[i+1] + arr[i+1]

    for i in range(len(cumulativeSums)):
        if cumulativeSums[i] == reverseCumulativeSums[i]:
            return 'YES'
    
    return 'NO'
    
if __name__ == '__main__':
    fptr = sys.stdout

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
