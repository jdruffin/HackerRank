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
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for index, char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            else:
                if node.children[char].is_end is True:
                    return word
                if index == len(word)-1:
                    return word
            node = node.children[char]
        node.is_end = True
        return 1

def noPrefix(words):
    # Write your code here
    trie = Trie()
    for word in words:
        if trie.insert(word) == word:
            print('BAD SET')
            print(word)
            return
    print('GOOD SET')
    



if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
