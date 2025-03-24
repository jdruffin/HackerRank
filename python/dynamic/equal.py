#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def equal(arr):
    # Write your code here
    def turnsTillMin(dp, array, minValue, iteration):
        turns = 0
        for value in array:
            value += iteration
            if value in dp:
                turns += dp[value]
            else:
                diff = value - minValue
                currentTurns = (diff // 5) + ((diff % 5) // 2) + (((diff % 5) % 2) //1)
                dp.update({value: currentTurns})
                turns+= currentTurns
        return turns


    sortedArray = sorted(arr, reverse=True)
    minValue = sortedArray[len(sortedArray)-1]

    dp = {}
    givenMin = turnsTillMin(dp, sortedArray, minValue, 0)
    givenMinMinus1 = turnsTillMin(dp, sortedArray, minValue, 1)
    givenMinMinus2 = turnsTillMin(dp, sortedArray, minValue, 2)
    givenMinMinus3 = turnsTillMin(dp, sortedArray, minValue, 3)
    givenMinMinus4 = turnsTillMin(dp, sortedArray, minValue, 4)

    return min(givenMin, givenMinMinus1, givenMinMinus2, givenMinMinus3, givenMinMinus4)


    '''
   5 4 3 2 1 0 
5  X X X X X 0
2  3 2 2 1 1 1  min(below, chocolateValue -row[i-chocolateValue] - 1)
1  5 4 3 2 1 1





    '''

    # dpDict = {}

    # dp[]
    # for i in range(-4, 1001):
    #     dpNext = []
        


    #     dp = dpNext    


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
