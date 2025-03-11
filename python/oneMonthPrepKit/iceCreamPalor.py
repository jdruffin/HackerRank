#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    counter = Counter(arr)
    for key in counter.keys():
        if counter[m-key] == 1 and m-key != key:
            return [arr.index(key)+1, arr.index(m-key) +1]
        if key*2 == m and counter[key] == 2:
            index = arr.index(key)
            return [index+1, arr.index(key, index+1) +1]

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
