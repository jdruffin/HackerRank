#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    count = 1
    while n != 0:
        if n%2 == 0:
            count *= 2
        n >>= 1
    return count

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
