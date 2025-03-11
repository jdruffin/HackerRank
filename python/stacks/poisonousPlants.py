#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    previousGreaterElement = []
    for index, plant in enumerate(p):
        # print('index' + str(index))
        if (index == 0):
            previousGreaterElement.append(-1)
        else:
            currentIndex = index -1
            if(plant < p[currentIndex]):
                previousGreaterElement.append(currentIndex)
            else:
                added = False
                while (plant >= p[previousGreaterElement[currentIndex]]):


                    
                    currentIndex = previousGreaterElement[currentIndex]
                    # print(str(currentIndex))
                    if(previousGreaterElement[currentIndex] == -1):
                        previousGreaterElement.append(-1)
                        added = True
                        break
                if not added :

                    previousGreaterElement.append(previousGreaterElement[currentIndex])


        print(previousGreaterElement)

    counts = []
    count =0
    for i, value in enumerate(previousGreaterElement):
        # print(i)
        # print(value)
        
        if value >=0:
            if value == previousGreaterElement[i-1]:
                count += 1
            else:
                counts.append(count)
                count = 0
    # print(counts)
    if(counts):
        return max(counts) + 1 if max(counts) else 0
    else:
        return 0





if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()


# 100 1 2     60 3 4 5 6 7 8 9 