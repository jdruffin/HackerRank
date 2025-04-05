#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import deque
def bfs(n, m, edges, s):
    # Write your code here
    adjacencyList = {i: [] for i in range(1,n+1)}
    
    for node1, node2 in edges:  
        adjacencyList[node1].append(node2)
        adjacencyList[node2].append(node1)
        
    distances = [int(-1) for i in range(n-1)]
    seenNodes = set([s])
    queue = deque([(s,0)])
    while queue:
        currentNode, distance = queue.popleft()
        for adjacentNode in adjacencyList[currentNode]:
            if adjacentNode not in seenNodes:
                queue.append((adjacentNode, distance+6))
                seenNodes.add(adjacentNode)
                if adjacentNode < s:
                    distances[adjacentNode-1] = distance+6
                else:
                    distances[adjacentNode-2] = distance+6
            
    
    return distances

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
