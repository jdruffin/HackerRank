#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
class Node:
    def __init__(self, data):
        self.data = data
        self.end = False
        self.children = {}

    def __str__(self):
        return str(self.data)  + str(self.end)


def noPrefix(words):
    # Write your code here
    root = Node(None)
    
    for word in words:
        currentNode = root
        for index, char in enumerate(word):

            
            if(char in currentNode.children):
                currentNode = currentNode.children[char]
                        
                if (currentNode.end is True or index == len(word)-1):
                    print('BAD SET')
                    print(word)
                    return                

            else:
                newNode = Node(char)
                currentNode.children.update({char: newNode})
                currentNode = newNode
                            
                if (currentNode.end is True):
                    print('BAD SET')
                    print(word)
                    return
                if(index == len(word)-1):
                    currentNode.end = True
    print('GOOD SET')
                
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
