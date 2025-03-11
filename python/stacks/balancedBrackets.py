#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    pairDictionary = {'}':'{', ']':'[', ')':'('}
    stack = []
    for char in s:
        if char in pairDictionary.values():
            stack.append(char)
        else:
            if len(stack) == 0 or stack.pop() != pairDictionary[char]:
                return 'NO'
    if(len(stack) == 0):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
