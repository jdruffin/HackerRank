#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    addedLengthRequired = 6 - n if 6 - n > 0 else 0
    digitRequired = 1
    lowerRequired = 1
    upperRequired = 1
    specialRequired = 1
    for char in password:
        if char.islower():
            lowerRequired = 0
        elif char.isupper():
            upperRequired = 0
        elif char.isdigit():
            digitRequired = 0
        elif char in ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'):
            specialRequired = 0

    otherAdds = digitRequired + upperRequired + lowerRequired + specialRequired
    return addedLengthRequired if addedLengthRequired > otherAdds else otherAdds

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
