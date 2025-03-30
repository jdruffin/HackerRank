#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def primeNumbersBelowIndex(q):
    primes = []
    boolArray = [True] * (104729) #10,000th prime value 104729

    boolArrayIndex = 2
    for _ in range(q):
        while boolArray[boolArrayIndex] is False:
            boolArrayIndex +=1

        primes.append(boolArrayIndex)
        for j in range(boolArrayIndex, 104729, boolArrayIndex):
            boolArray[j] = False

        boolArrayIndex +=1
    return primes

def waiter(numbers, q):
    # Write your code here
    answers = []
    a=[]
    b=[]

    primes = primeNumbersBelowIndex(q)

    for prime in primes:
        a=[]
        while numbers:
            value = numbers.pop()
            if value % prime == 0:
                b.append(value)
            else:
                a.append(value)
        while(b):
            answers.append(b.pop())
        numbers = a

    while numbers:
        answers.append(numbers.pop())

    return answers

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
