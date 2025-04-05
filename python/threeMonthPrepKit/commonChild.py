#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    dp = [[0 for i in range(len(s1)+1)] for i in range(len(s2) +1)]

    for i in range(len(s1)-1, -1, -1):
        for j in range(len(s2)-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1] +1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

if __name__ == '__main__':
    fptr = sys.stdout

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
