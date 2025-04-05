#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    convertAsciiToWeight = 96
    ordSums = [ord(s[0])-convertAsciiToWeight]
    currOrd = ord(s[0])
    for i in range(1, len(s)):
        if ord(s[i]) == currOrd:
            ordSums.append(ordSums[-1] + ord(s[i]) - convertAsciiToWeight)
        else:
            ordSums.append(ord(s[i]) -convertAsciiToWeight)
            currOrd = ord(s[i])

    ordSumsSet = set(ordSums)
    returnArray = []
    for query in queries:
        if query in ordSumsSet:
            returnArray.append('Yes')
        else:
            returnArray.append('No')

    return returnArray
if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
