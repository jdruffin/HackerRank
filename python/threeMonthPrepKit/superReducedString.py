#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    charList = []
    for char in s:
        charList.append(char)
    
    removed = True
    while removed:
        i = 0
        removed = False
        while i < len(charList)-1:
            if charList[i] != 'X' and charList[i] == charList[i+1]:
                charList[i] = 'X'
                charList[i+1]  = 'X'
                i += 2
                removed = True
            else:
                i += 1
        charList = [x for x in charList if x != 'X']
    
    return ''.join(charList) if len(charList) > 0 else 'Empty String'


if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
