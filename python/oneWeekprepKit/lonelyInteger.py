#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    counter = Counter(a)

    return counter.most_common()[-1][0]

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
