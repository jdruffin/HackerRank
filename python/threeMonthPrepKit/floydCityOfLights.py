#!/bin/python3

import math
import os
import random
import re
import sys


def floyd(nodes, road_from, road_to, road_weight, queries):

    dp = [[9999999999 for _ in range(nodes)] for _ in range(nodes) ]

    for i in range(len(road_from)):
        dp[road_from[i]][road_to[i]] = road_weight[i]

    for i in range(nodes):
        dp [i][i] = 0

    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                if dp[j][k] > dp[j][i] + dp[i][k]:
                    dp[j][k] = dp[j][i] + dp[i][k]

    returnArray = []
    for query in queries:
        fromNode, toNode = query
        if dp[fromNode][toNode] == 9999999999:
            returnArray.append(-1)

        else:
            returnArray.append(dp[fromNode][toNode])
    
    return returnArray
if __name__ == '__main__':
    fptr = sys.stdout

    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        x, y, z =  map(int, input().rstrip().split())
        road_from[i], road_to[i], road_weight[i] = x-1, y-1, z

    q = int(input().strip())

    queries = []

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])-1

        y = int(first_multiple_input[1])-1
        queries.append([x,y])

    answers = floyd(road_nodes, road_from, road_to, road_weight, queries)

    for answer in answers:
        fptr.write(str(answer) + '\n')

    fptr.close()
