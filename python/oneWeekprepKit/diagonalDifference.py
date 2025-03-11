#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leftToRight = rightToLeft = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i == j):
                leftToRight += arr[i][j]
            if(j + i == len(arr)-1):

                rightToLeft += arr[i][j]

    return abs(leftToRight - rightToLeft)

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
