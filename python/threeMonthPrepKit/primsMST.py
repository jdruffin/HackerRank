#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#
import heapq

def prims(n, edges, start):
    # Write your code here
    addedNodes = set([start])
    edges.sort(key = lambda x: x[-1])
    totalWeight = 0
    while len(addedNodes) != n:
        for i in range(len(edges)):
            node1, node2, weight = edges[i]
            if node1 in addedNodes and node2 not in addedNodes:
                addedNodes.add(node2)
                totalWeight+= weight
                del edges[i]
                break
            elif node2 in addedNodes and node1 not in addedNodes:
                addedNodes.add(node1)
                totalWeight+= weight
                del edges[i]
                break
    return totalWeight

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
