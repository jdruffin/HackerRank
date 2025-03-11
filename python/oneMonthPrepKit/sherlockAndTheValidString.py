#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    values = sorted(Counter(s).values())

    if len(set(values)) == 1:
        return 'YES'
    
    if values[0] == 1 and values[1] == values[-1]:
        return 'YES'

    if values[-1] - values[-2] == 1 and values[0] == values[-2]:
        return 'YES'

    return 'NO'



if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
