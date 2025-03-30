#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    sortedGrid = []
    for row in grid:
        sortedGrid.append(''.join(sorted(row)))

    for i in range(len(sortedGrid[0])):
        column = ''
        for j in range(len(sortedGrid)):
            column+=sortedGrid[j][i]
        if(column != ''.join(sorted(column))):
            return 'NO'
        
    return 'YES'

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
