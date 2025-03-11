#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = Node(1)
        self.current = self.root
        self.nextParentNode = []

    def add(self, val):  
        val1 = Node(val[0])
        val2 = Node(val[1])
        self.nextParentNode.append(val1)
        self.nextParentNode.append(val2)

        while self.current.info == -1:
            self.current = self.nextParentNode.pop(0)

        self.current.left = val1
        self.current.right = val2
        self.current = self.nextParentNode.pop(0)

def inOrder(root):
    answer = []
    def recursion(root):
        if root.left.info != -1:
            recursion(root.left)
            answer.append(root.info)
        else:
            answer.append(root.info)
            if root.right.info != -1:
                recursion(root.right)
        if root.left.info != -1 and root.right.info != -1:
            recursion(root.right)
    recursion(root)

    return answer

def swap(root, query, currLevel):
    if currLevel % query == 0:
        leftTemp = root.left
        rightTemp = root.right

        root.left = rightTemp
        root.right = leftTemp
    if root.left.info != -1:
        swap(root.left, query, currLevel+1)
    if root.right.info != -1:
        swap(root.right, query, currLevel+1)

def swapNodes(indexes, queries):
    # Write your code here
    tree = BinarySearchTree()
    for i in range(len(indexes)):
        tree.add(indexes[i])
    
    returnArray = []
    for i in range(len(queries)):
        swap(tree.root, queries[i], 1)
        returnArray.append(inOrder(tree.root))
    return returnArray

sys.setrecursionlimit(15000)

fptr = sys.stdout

n = int(input().strip())

indexes = []

for _ in range(n):
    indexes.append(list(map(int, input().rstrip().split())))

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = int(input().strip())
    queries.append(queries_item)

result = swapNodes(indexes, queries)

fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
fptr.write('\n')

fptr.close()
