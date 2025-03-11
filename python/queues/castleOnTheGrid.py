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


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None


def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    possiblePaths = []
    queue = deque()
    queue.append(Node([startX, startY]))

    seenNodes = set()
    found = False
    while queue:
        currentNode = queue.popleft()
        currentX, currentY = currentNode.value
        seenNodes.add((currentX, currentY))
        for direction in directions:
            endPositionX = currentX + direction[0]
            endPositionY = currentY + direction[1]

            newNode = Node([endPositionX, endPositionY])
            newNode.parent = currentNode

            if (endPositionX == goalX and endPositionY == goalY):
                pathToAdd = []
                while (newNode is not None):
                    pathToAdd.append(newNode.value)
                    newNode = newNode.parent
                possiblePaths.append(pathToAdd)
                print('possiblePaths' + str(possiblePaths))
                found = True
                break
            if (found is False and 0 <= endPositionY <= len(grid)-1 and
                0 <= endPositionX <= len(grid)-1 and
                    grid[endPositionX][endPositionY] != 'X' and
                    (endPositionX, endPositionY) not in seenNodes):

                queue.append(newNode)

    print(possiblePaths)
    numOfTurns = []

    for path in range(len(possiblePaths)):
        turns = 0
        currentPath = possiblePaths[path]
        currentDirection = [currentPath[0][0] - currentPath[1]
                            [0], currentPath[0][1] - currentPath[1][1]]
        for position in range(len(currentPath)-1):
            newDirection = [currentPath[position][0] - currentPath[position+1]
                            [0], currentPath[position][1] - currentPath[position+1][1]]
            if (newDirection != currentDirection):
                turns += 1
                currentDirection = newDirection
        numOfTurns.append(turns)

    return min(numOfTurns) + 1


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
