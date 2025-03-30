#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    sortedArray = [[] for i in range(len(arr))]
    for i in range(len(arr)):
        index, string = arr[i]

        if i < len(arr)//2:
            sortedArray[int(index)].append('-')
        else:
            sortedArray[int(index)].append(string)

    res = [y for x in sortedArray for y in x]
    print(' '.join(res))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
