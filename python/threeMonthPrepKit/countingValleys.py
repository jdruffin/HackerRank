#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    currentHeight = 0
    valleyCount = 0
    for step in path:
        if step == 'U':
            currentHeight += 1
        if step == 'D':
            if currentHeight == 0:
                valleyCount += 1
            currentHeight -= 1
            
    return valleyCount
if __name__ == '__main__':
    fptr = sys.stdout

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
