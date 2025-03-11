import math
import os
import random
import re
import sys

# def isPalindrome(s):
#     midPoint = (len(s) //2)
#     for i in range(midPoint):
#         if (s[i] != s[len(s)-1-i]):
#             return False
#     return True
        
    

# def palindromeIndex(s):
#     # Write your code here
#     if (isPalindrome(s)):
#         print("was already")
#         return -1
#     for i in range(len(s)):
#         tempString = s[0:i]+s[i+1:len(s)]
#         print(tempString)
#         if (isPalindrome(tempString)):
#             return i
#     return -1


def isPalindrome(s):
    midPoint = (len(s) //2)
    for i in range(midPoint):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True
        
def indexWhereFailed(s):
    midPoint = (len(s) //2)
    for i in range(midPoint):
        if (s[i] != s[len(s)-1-i]):
            return i

def palindromeIndex(s):
    # Write your code here
    if (isPalindrome(s)):
        return -1
    else:
        i = indexWhereFailed(s)
        i2 = len(s) -1 -i
        if(isPalindrome(s[0:i]+s[i+1:len(s)])):
            return i
        elif(isPalindrome(s[0:i2]+s[i2+1:len(s)])):
            return i2
        else:
            return -1

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
