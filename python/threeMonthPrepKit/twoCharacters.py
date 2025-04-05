#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    comb = list(combinations(set(s), 2))
    len_max = 0
    
    for i in comb:
        txt = s
        txt = "".join(c for c in txt if c in i)
        if re.search(r"(.)\1", txt):
            continue
        else:
            if len(txt) > len_max:
                len_max = len(txt)
    
    return len_max

if __name__ == '__main__':
    fptr = sys.stdout

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
