#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    powersOfTwo = [2**n for n in range(64)]
    turns = 0
    while n != 1:
        turns += 1
        if n in powersOfTwo:
            n //= 2
        else:
            validValues = [x for x in powersOfTwo if x < n]
            reducedBy = max(validValues)
            n -= reducedBy

    return 'Richard' if turns%2==0 else 'Louise'

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
