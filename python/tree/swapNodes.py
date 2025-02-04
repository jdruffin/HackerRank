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
def swapNodes(indexes, queries):
    def inOrder(root):
        #Write your code here
        answer = []
        def recursion(root):
            if root is not None:
                if root.left is not None:
                    recursion(root.left)
                    answer.append(root.info)
                else:
                    answer.append(root.info)
                if root.right is not None:
                    recursion(root.right)

        recursion(root)

        returnString = ''
        for i in answer:
            returnString += str(i) + ' '
        print(returnString)
    
    #swap
    inOrder(root)

if __name__ == '__main__':
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

    print(indexes)
    print(queries)
    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
