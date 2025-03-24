#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#



def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 - x2 > 0:
        return 'YES' if v1-v2 < 0 and (x1 - x2) % (v1 - v2) == 0 else 'NO'
    elif x1 - x2 > 0:
        return 'YES' if v1-v2 > 0 and (x1 - x2) % (v1 - v2) == 0 else 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
