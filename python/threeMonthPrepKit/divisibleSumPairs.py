#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    for i in range(len(ar)):
        ar[i] %= k
    counter = Counter(ar)

    print(counter)

    pairs = 0
    for key in counter:
        if k-key in counter and key != k-key:
            pairs += counter[key] * counter[k-key] /2
        elif key == 0 or k // key == 2:
            pairs += (counter[key] * (counter[key] -1)) //2

    return int(pairs)

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
