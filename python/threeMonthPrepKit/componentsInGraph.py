#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    parent = [i for i in range(len(gb)*2 +1)]
    rank = [1 for i in range(len(gb)*2 +1)]
    
    def findParent(node):
        while node != parent[node]:
            node = parent[node]
        return node
    
    def union(node1, node2):
        node1 = findParent(node1)
        node2 = findParent(node2)
        
        if node1 == node2:
            return
        
        if rank[node1] < rank[node2]:
            node1, node2 = node2, node1
            
        parent[node2] = node1
        rank[node1] += rank[node2]
        
        
    for node1, node2 in gb:
        union(node1, node2)
        

    minValue = 9999999999
    maxValue = 0
    for i in range(len(parent)):
        if rank[findParent(i)] > 1 and rank[findParent(i)] < minValue:
            minValue = rank[findParent(i)]
        if rank[i] > maxValue:
            maxValue = rank[findParent(i)]
        
    return [minValue, maxValue]
        

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
