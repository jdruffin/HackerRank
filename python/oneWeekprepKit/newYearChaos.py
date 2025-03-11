#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    bribes = 0
    for index, value in enumerate(q):
        position = index+1
        if (value > position + 2):
            print("Too chaotic")
            return
        else:
            for j in range(max(0,value-2), index):
                if (q[j] > value):
                    bribes +=1
    print(bribes)
    


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
