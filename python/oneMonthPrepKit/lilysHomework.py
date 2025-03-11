#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here

    def numberOfSwitches(givenList, expectedList):
        count = 0

        indexHashMap = {}
        for i in range(len(givenList)):
            indexHashMap[givenList[i]] = i

        for i in range(len(givenList)):
            if givenList[i] != expectedList[i]:

                originalIndex = indexHashMap[expectedList[i]]
                indexHashMap[givenList[i]] = originalIndex

                givenList[i], givenList[originalIndex] = givenList[originalIndex], givenList[i]


                count+=1
        
        return count


    ascendingList = sorted(arr)
    descendingList = sorted(arr, reverse= True)

    ascendingListCount = numberOfSwitches(arr, ascendingList)
    descendingListCount = numberOfSwitches(arr, descendingList)
    print(ascendingListCount)
    print(descendingListCount)

    return min(ascendingListCount, descendingListCount)
    

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
