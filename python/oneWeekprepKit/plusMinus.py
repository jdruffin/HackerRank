#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    postive = negative = zero = 0
    for value in arr:
        if value > 0:
            postive+=1
        elif value < 0:
            negative+=1
        else:
            zero +=1

    print(f"{postive/len(arr):.6f}")
    print(f"{negative/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
