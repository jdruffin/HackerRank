#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    ranges = []
    i = len(prices)-1
    while i >= 0:
        currValues = [prices[i]]
        while i-1 >= 0 and prices[i-1] < currValues[0]:
            currValues.append(prices[i-1])
            i-=1
        
        ranges.append(currValues)
        i-=1
    
    totalSum = 0
    for sequence in ranges:
        sequenceSum = 0
        for i in range(1, len(sequence)):
            sequenceSum += sequence[0] - sequence[i]
        totalSum += sequenceSum

    return totalSum


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
