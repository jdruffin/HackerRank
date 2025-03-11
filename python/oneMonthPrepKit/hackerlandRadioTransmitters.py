#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here

    x.sort()
    answers = []
    i=0
    while i<len(x):
        startingValue = x[i]
        while i+1 < len(x) and x[i+1] - startingValue <= k:
            i+=1
        answers.append(i)

        newValue = x[i]
        while i<len(x) and x[i] - newValue <=k:
            i+=1

    return len(answers) 
    



if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
