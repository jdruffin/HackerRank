#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    answer = []
    for grade in grades:
        if grade < 38:
            answer.append(grade)
        elif grade % 5 >= 3 :
            answer.append(grade + 5-(grade%5))
        else:
            answer.append(grade)

    return answer
if __name__ == '__main__':
    fptr = sys.stdout

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
