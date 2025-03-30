#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    count = 0
    for windowSize in range(len(s)):
        dicts = []
        for i in range(len(s) - windowSize):
            dicts.append(Counter(s[i:i+windowSize+1]))
        
        for i in range(len(dicts)):
            for j in range(i+1, len(dicts)):
                if dicts[i] == dicts[j]:
                    count += 1            

    return count

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
