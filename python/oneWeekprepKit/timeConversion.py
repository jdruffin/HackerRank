#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    hours, minutes, temp = s.split(":")
    seconds = temp[:2]
    pmBool = 1 if temp[2:] == 'PM' else 0
    if(hours == '12'):
        hours = "0"

    answer = f"{(int(hours) + (12 * (pmBool))
                 ):02d}"  + ":" + f"{int(minutes):02d}" + ":" + f"{int(seconds):02d}"

    return answer


if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
