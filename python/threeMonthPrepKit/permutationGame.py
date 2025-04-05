#!/bin/python3

import math
import os
import random
import re
import sys
from functools import lru_cache
from itertools import combinations


comb = list(combinations(set(s), 2))

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

@lru_cache(None)
def perm(t):
    if all(a<b for a,b in combinations(t, 2)):
        return 1
    elif any( 1 == perm(t[:i]+t[i+1:]) for i in range(len(t))):
        return 0
    else:
        return 1
   
def permutationGame(arr):
    return 'Alice' if perm(tuple(arr)) == 0 else 'Bob'

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
