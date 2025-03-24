#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    count = 0
    for i in range(len(s)//3):
        if s[i*3] != 'S':
            count +=1
        if s[i*3+1] != 'O':
            count +=1
        if s[i*3+2] != 'S':
            count +=1
    return count
    
if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
