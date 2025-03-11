#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    returnString = []
    for char in s:
        if (char.islower()):
            returnString.append(chr((ord(char) - 97 + (k % 26)) % 26 + 97))
        elif (char.isupper()):
            returnString.append(chr((ord(char) - 65 + (k % 26)) % 26 + 65))
        else:
            returnString.append(char)

    return ''.join(returnString)


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
