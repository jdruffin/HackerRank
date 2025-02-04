class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def topView(root):
    #Write your code here
    dictionary = {}
    lateralPosition = 0
    depth = 0
    def recursion(root, lateralPosition,depth):
        if root is not None:
            if lateralPosition in dictionary.keys():
                temp = dictionary[lateralPosition]
                temp.append((depth, root.info))
                dictionary.update({lateralPosition: temp})
            else:
                dictionary.update({lateralPosition:[(depth,root.info)]})

            if root.left is not None:
                recursion(root.left, lateralPosition-1, depth +1)
            if root.right is not None:
                recursion(root.right, lateralPosition+1, depth +1)
    recursion(root, lateralPosition, depth)

    returnString = ''
    keys = list(dictionary.keys())
    keys.sort()

    for key in keys:
        values = list(dictionary[key])
        values.sort()
        returnString = returnString + str(values[0][1]) + ' '
    print(returnString)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)

