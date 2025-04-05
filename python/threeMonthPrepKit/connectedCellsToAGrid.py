#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    visitedPositions = set()
    region = set()
    
    def dfs(pos):
        row,col = pos
        
        visitedPositions.add((row, col))
        region.add((row,col))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,-1], [1,1], [-1,1], [-1,-1]]
        for direction in directions:
            dx, dy = direction
            newRow, newCol = row + dx, col + dy
            if newCol >=0 and newCol < len(matrix[0]) and newRow >= 0 and newRow < len(matrix) and (newRow,newCol) not in visitedPositions and matrix[newRow][newCol] == 1:
                dfs((newRow, newCol))
        
        
    maxRegion = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row,col) not in visitedPositions and matrix[row][col] == 1:
                dfs((row,col))
                maxRegion = max(maxRegion, len(region))
                print(len(region))
                region.clear()
                
    return maxRegion
  
if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
