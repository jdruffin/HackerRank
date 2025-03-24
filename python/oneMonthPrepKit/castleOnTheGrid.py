#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#


def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    seenNodes = set()
    queue = deque([[startX, startY, 0]])
    turns = 0
    while queue:

        currX, currY, turns = queue.popleft()
        turns += 1

        for direction in directions:
            x, y = currX, currY

            while True:
                x += direction[0]
                y += direction[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == '.':

                    if (x == goalX and y == goalY):
                        return turns
                    elif (x, y) not in seenNodes:
                        seenNodes.add((x, y))
                        queue.append([x, y, turns])
                else:
                    break


if __name__ == "__main__":
    fptr = sys.stdout

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + "\n")

    fptr.close()
