#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    indexOfPage = p//2 if p%2 ==0 else (p-1)//2
    lengthOfBook = n//2 if n%2 ==0 else (n-1)//2
    return min(lengthOfBook - indexOfPage, indexOfPage)

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
