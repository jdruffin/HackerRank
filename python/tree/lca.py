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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    #Enter you code here.
    current = root
    v1Parents = [root]
    while (v1 < current.info and current.left is not None) or (v1 > current.info and current.right is not None):
        if v1 < current.info:
            current = current.left
        else:
            current = current.right
        v1Parents.append(current)

    current = root
    v2Parents = [root]
    while (v2 < current.info and current.left is not None) or (v2 > current.info and current.right is not None):
        if v2 < current.info:
            current = current.left
        else:
            current = current.right
        v2Parents.append(current)

    v1Parents.reverse()
    for parent in v1Parents:
        if parent in v2Parents:
            return parent
    return root



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
