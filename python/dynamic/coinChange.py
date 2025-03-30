#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#


def getWays(n, c):
    # Write your code here
    sortedCoins = sorted(c, reverse=True)
    dp = [0 for i in range(n+1)]
    dp2 = [0 for i in range(n+1)]

    for coin in sortedCoins:
        for i in range(n+1):
            if i == 0:
                dp[i] = 1
            else:
                if i - coin < 0:
                    dp[i] = 0
                else:
                    dp[i] = dp2[i] + dp[i-coin]
        
        dp2 = dp
    
    return dp[n]

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
