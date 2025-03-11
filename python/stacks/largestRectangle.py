#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    pointer1 = 0
    pointer2 = 0
    answer = 0

    for i in range(len(h)):
        minHeight = h[i]
        pointer1=i
        pointer2 = i
        while pointer1 >= 0 and h[pointer1] >= minHeight:
            pointer1 -= 1
        
        while pointer2 < len(h) and h[pointer2] >= minHeight:
            pointer2 += 1

        answer = max(answer, (pointer2 - pointer1 -1) * minHeight)

    return answer
    # while pointer1 < len(h):
    #     pointer2 = pointer1 +1
    #     currentHeight = h[pointer1]
    #     while(pointer2 < len(h) and h[pointer2]>= currentHeight):
    #         pointer2 += 1
    #     answer = max(answer, (pointer2 - pointer1) * currentHeight)

    #     pointer1 += 1
    

     


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
