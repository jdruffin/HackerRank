#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack = []
    returnValues = []
    maximum = [0]
    for operation in operations:
        values = list(map(int, operation.split(' ')))
        if values[0] == 1:
            stack.append(values[1])
            if(values[1] >= maximum[-1]):
                maximum.append(values[1])
        elif values[0] == 2:
            removedValue = stack.pop()
            if removedValue == maximum[-1]:
                maximum.remove(removedValue)
        else:
            returnValues.append(maximum[-1])
    return returnValues

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
