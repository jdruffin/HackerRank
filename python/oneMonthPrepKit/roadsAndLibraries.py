#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    def pathsPerGroup(city, visited):
        paths = 0
        queue = [city]
        visited.add(city)

        while queue:
            currentCity = queue.pop()
            if city in adjacencyList.keys():
                for adjacentCity in adjacencyList[city]:
                    if adjacentCity not in visited:
                        queue.append(adjacentCity)
                        visited.add(adjacentCity)
                        paths += 1
        return paths

    if c_lib < c_road:
        return n * c_lib
    else:
        adjacencyList = {}
        for path in cities:
            city1, city2 = path
            if city1 not in adjacencyList.keys():
                adjacencyList.update({city1: [city2]})
            else:
                adjacencyList[city1].append(city2)
            if city2 not in adjacencyList.keys():
                adjacencyList.update({city2: [city1]})
            else:
                adjacencyList[city2].append(city1)

        numOfGroups = 0
        numOfPaths = 0

        visited = set()

        for city in range(1, n+1):
            if city not in visited:
                numOfPaths += pathsPerGroup(city, visited)
                numOfGroups += 1

        return (numOfGroups * c_lib) + (numOfPaths* c_road)

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
