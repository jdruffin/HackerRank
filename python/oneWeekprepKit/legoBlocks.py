#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    mod = 10**9 +7
    totalArrangements = [0,1,2,4,8]

    while len(totalArrangements) <= m:
        totalArrangements.append(sum(totalArrangements[-4:])%mod)
    
    print(totalArrangements)

    totalCombinations = []
    for i in range(m+1):
        totalCombinations.append(pow(totalArrangements[i], n, mod))

    invalids=[0,0]
    for i in range(2, m+1):
        invalid = []
        for left in range(1,i):
            l = totalCombinations[left] - invalids[left]
            r = totalCombinations[i-left]
            invalid.append(l*r)
        invalids.append(sum(invalid) % mod)

    return (totalCombinations[m] - invalids[m]) % mod

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
