#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minScore = maxScore = scores[0]

    answer = [0 for i in range(2)]
    for i in range(1, len(scores)):
        if scores[i] < minScore:
            answer[1] += 1
            minScore = scores[i]
        elif scores[i] > maxScore:
            answer[0] += 1
            maxScore = scores[i]
    
    return answer

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
