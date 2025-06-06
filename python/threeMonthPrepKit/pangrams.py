#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    letters = set(s.lower().replace(' ', ''))
    return 'pangram' if len(letters) == 26 else 'not pangram'

if __name__ == '__main__':
    fptr = sys.stdout
    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
