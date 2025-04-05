#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    # Write your code here
    returnValue = 0
    currentEnergy = 0
    for i in range(len(arr)):
        newEnergy = 0 
        if currentEnergy < arr[i]:
            newEnergy = currentEnergy - (arr[i] - currentEnergy)
            while newEnergy < 0:
                returnValue += 1
                newEnergy += (2**i)*2
        else:
            newEnergy = currentEnergy + currentEnergy - arr[i]
        
        currentEnergy = newEnergy

    return returnValue
if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
