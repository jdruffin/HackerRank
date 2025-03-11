#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    middlePoint = len(matrix)//2
    MaxValue = 0
    for i in range(0, middlePoint):
        for j in range(0, middlePoint):
            MaxValue += max(matrix[i][j], matrix[i][len(matrix)-1-j], matrix[len(matrix)-1-i][j], matrix[len(matrix)-1-i][len(matrix)-1-j])
            
    return MaxValue

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
