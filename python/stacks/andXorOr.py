#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def andXorOr(a):
    # Write your code here
    # nextSmallestIndex = [-1] * len(a)
    # for i in range(len(a)-2, -1, -1):
    #     currentValue = a[i]
    #     nextValueOver = a[i+1]
    #     if(nextValueOver < currentValue):
    #         nextSmallestIndex[i] = i+1
    #     else:
    #         j=i+1
    #         while(currentValue < a[nextSmallestIndex[j]] and nextSmallestIndex[j] != -1):
    #             j = nextSmallestIndex[i]
    #         nextSmallestIndex[i] = nextSmallestIndex[j]
    # print(nextSmallestIndex)


    # possiblePairs = []
    # for i, value in enumerate(nextSmallestIndex):
    #     smallest = a[i]
    #     secondSmallest = a[i]
    #     while(value != -1):
    #         if(a[value] < smallest):
    #             secondSmallest = smallest
    #             smallest = a[value]
    #         elif(a[value] < secondSmallest):
    #             secondSmallest= a[value]
    #         possiblePairs.append([smallest, secondSmallest])

    #         value = nextSmallestIndex[value]
    # print(possiblePairs)


    # possibleValues = []
    # for value1, value2 in possiblePairs:
    #     currentAnswer = (((value1 & value2) ^ (value1 | value2)) & (value1 ^ value2))
    #     possibleValues.append(currentAnswer)
    # print(possibleValues)
        
    # return max(possibleValues)
    answer = 0
    stack = []
    for value in a:
        while stack:
            answer = max(answer, (((value & stack[-1]) ^ (value | stack[-1])) & (value ^ stack[-1])))
            if(value < stack[-1]):
                stack.pop()
            else:
                break
    
        stack.append(value)
    return answer



if __name__ == '__main__':
    fptr = sys.stdout

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
