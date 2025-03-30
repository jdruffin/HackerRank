#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    hashmap = {}
    for index, value in enumerate(arr):
        hashmap.update({value: index})
    
    arr.sort(reverse = True)
    
    currentIndex = len(arr)-1
    turns = 0
    for value in arr:
        if hashmap[value] <= currentIndex:
            currentIndex = hashmap[value]
            turns += 1
        if currentIndex == 0:
            return 'ANDY' if turns % 2 == 0 else 'BOB'


if __name__ == '__main__':
    fptr = sys.stdout

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
