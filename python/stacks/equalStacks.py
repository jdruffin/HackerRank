#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def equalStacks(h1, h2, h3):
    x1, x2, x3 = sum(h1), sum(h2), sum(h3)
    q1, q2, q3 = deque(h1), deque(h2), deque(h3)
    while True:
        if x1 == x2 and x2 == x3:
            break
        elif x1 >= x2 and x1 >= x3:
            x1 -= q1.popleft()
        elif x3 >= x2 and x3 >= x1:
            x3 -= q3.popleft()
        elif x2 >= x1 and x2 >= x3:
            x2 -= q2.popleft()
    return x1


if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
