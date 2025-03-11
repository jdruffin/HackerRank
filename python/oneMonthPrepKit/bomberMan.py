#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        return grid
    fullbombs = ['O' * len(grid[0]) for i in range(len(grid))]
    if n%2 == 0:
        return fullbombs

    state2 = [row[:] for row in fullbombs]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                if i - 1 >=0:
                    state2[i-1] = state2[i-1][:j] + '.' + state2[i-1][j+1:]
                if i + 1 <= len(grid)-1:
                    state2[i+1] = state2[i+1][:j] + '.' + state2[i+1][j+1:]
                if j + 1 <= len(grid[0])-1:
                    state2[i] = state2[i][:j+1] + '.' + state2[i][j+2:]
                if j - 1 >= 0:
                    state2[i] = state2[i][:j-1] + '.' + state2[i][j:]
                state2[i] = state2[i][:j] + '.' + state2[i][j+1:]

    state3 = [row[:] for row in fullbombs]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if state2[i][j] == 'O':
                if i - 1 >=0:
                    state3[i-1] = state3[i-1][:j] + '.' + state3[i-1][j+1:]
                if i + 1 <= len(grid)-1:
                    state3[i+1] = state3[i+1][:j] + '.' + state3[i+1][j+1:]
                if j + 1 <= len(grid[0])-1:
                    state3[i] = state3[i][:j+1] + '.' + state3[i][j+2:]
                if j - 1 >= 0:
                    state3[i] = state3[i][:j-1] + '.' + state3[i][j:]
                state3[i] = state3[i][:j] + '.' + state3[i][j+1:]

    if n % 4 == 1:
        return state3

    if n %4 == 3:
        return state2

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
