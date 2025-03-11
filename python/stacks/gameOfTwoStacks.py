#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    stack = []

    countA = 0
    countB = 0
    answer = 0
    totalValue = 0

    for value in a:
        if (value + totalValue <= maxSum):
            stack.append(value)
            totalValue+=value
            countA+=1
            answer+=1
        else:
            break
  
    for value in b:
        totalValue += value
        countB +=1
        while len(stack) != 0 and totalValue > maxSum:
            countA -=1
            totalValue -= stack.pop()
        if totalValue <= maxSum and answer < countA + countB:
            answer = countA + countB

    return answer

if __name__ == '__main__':
    fptr = sys.stdout

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
