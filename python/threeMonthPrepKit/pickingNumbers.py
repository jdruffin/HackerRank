#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    counter = Counter(a)

    answer = 0
    for key in counter:
        if key+1 in counter:
            answer = max(answer, counter[key] + counter[key+1])
        else:
            answer = max(answer, counter[key])

    return answer

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
