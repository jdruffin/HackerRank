#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    if all(x == 1 for x in s):
        if len(s) % 2 == 1:
            return "Second"
        else:
            return "First"
    else:
        balance = 0
        for val in s:
            balance ^= val
        if balance == 0:
            return "Second"
        else:
            return "First"

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
