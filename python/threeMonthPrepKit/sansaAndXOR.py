#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # Write your code here

    # valuesToXOR = []
    # valuesToXOR.extend(arr)
    # numOfValues = 2
    # while numOfValues <= len(arr):
    #     for i in range(len(arr)-numOfValues+1):
    #         result = arr[i]
    #         for j in range(1,numOfValues):
    #             result ^= arr[i+j]
    #         valuesToXOR.append(result)    
    #     numOfValues += 1
    # returnResult = valuesToXOR[0]
    # for i in range(1, len(valuesToXOR)):
    #     returnResult ^= valuesToXOR[i]
    # return returnResult


    # returnResult = 0
    # for i in range(len(arr)):
    #     currentValue = arr[i]
    #     returnResult ^= currentValue
    #     for j in range(i+1, len(arr)):
    #         currentValue ^= arr[j]
    #         returnResult^= currentValue
    # return returnResult

    if (len(arr) % 2 == 0):
        return 0
    else:
        answer = 0
        for i in range(0,len(arr), 2):
            answer ^= arr[i]
        return answer

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
