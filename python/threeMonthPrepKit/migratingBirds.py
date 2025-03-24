#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here

    counts = [0 for i in range(5)]

    for bird in arr:
        counts[bird-1] += 1
    
    maxNumber = 0
    for count in counts:
        if count > maxNumber:
            maxNumber = count
    
    return counts.index(maxNumber) +1
            


if __name__ == '__main__':
    fptr = sys.stdout

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
