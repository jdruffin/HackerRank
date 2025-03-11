#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import heapq
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(set(ranked), reverse=True)
    rank = []
    length = len(ranked)
    
    i = length - 1
    
    for score in player:
        while i >= 0 and score >= ranked[i]:
            i -= 1
        rank.append(i + 2)
    
    return rank
        

if __name__ == '__main__':
    fptr = sys.stdout

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
