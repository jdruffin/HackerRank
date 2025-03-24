#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    size = 1
    i = 0
    firstValue = ''
    while size < len(s)//2:
        if int(s[(i+1)*size:(i+1)*size + size]) - int(s[i*size:i*size + size]) == 1 and s[(i+1)*size] != '0' and s[i*size] != '0':
            if i == 0:
                firstValue = s[i*size:i*size + size]
            i += 1
        else:
            size +=1
            i = 0
        if (i+1)*size + size == len(s):
            print('YES ' + str(firstValue))
            return
    print('NO')
    return


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
