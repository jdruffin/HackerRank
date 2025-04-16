#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    firstHeap = []
    secondHeap = []

    for value in a:
        if len(firstHeap) == len(secondHeap):
            


if __name__ == '__main__':
    fptr = sys.stdout

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
