#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    currentIndex = 0
    count = 0
    while currentIndex < len(arr):
        furthestOne = -1
        for i in range(-k+1,k):
            if currentIndex + i >=0 and currentIndex + i <= len(arr)-1 and arr[currentIndex + i] == 1:
                furthestOne = currentIndex +i
        if furthestOne == -1:
            return -1
        else:
            currentIndex = furthestOne + k
            count += 1
    return count

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
