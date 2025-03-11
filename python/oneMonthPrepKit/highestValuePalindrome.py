#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def createPalindrome(s):
    indexWhereChanged = set([])
    count = 0
    midpoint = len(s) //2
    for i in range(midpoint):
        if s[i] > s[len(s) -i -1]:
            s = s[:len(s) -i -1] + s[i] + s[len(s) -i:]
            indexWhereChanged.add(i)
            count += 1
        elif s[i] < s[len(s) -i -1]:
            s = s[:i] + s[len(s) -i -1] + s[i+1:]
            indexWhereChanged.add(i)
            count+= 1

    return (s, count, indexWhereChanged)

def highestValuePalindrome(originalString, n, k):
    # Write your code here
    s, count, changes = createPalindrome(originalString)

    if(count > k):
        return '-1'

    for i in range(len(s)+1//2):
        if(s[i] != '9'):
            if(i in changes):
                if(k-count >=1):
                    s = s[:i] + '9' + s[i+1:len(s) -i -1] + '9' + s[len(s)-i:]
                    count+= 1
            else:
                if(i == len(s) -i -1):
                    if(k-count >=1):
                        s = s[:i] + '9' + s[len(s)-i:]
                        count+= 1
                else:
                    if(k-count >=2):
                        s = s[:i] + '9' + s[i+1:len(s) -i -1] + '9' + s[len(s)-i:]
                        count+= 2
    
    return s



if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
