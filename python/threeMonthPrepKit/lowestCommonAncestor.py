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
    v1Path = [root]
    currNode1 = root
    while currNode1.info != v1:
        if v1 > currNode1.info:
            currNode1 = currNode1.right
        else:
            currNode1 = currNode1.left
        v1Path.append(currNode1)


    v2Path = [root]
    currNode2 = root
    while currNode2.info != v2:
        if v2 > currNode2.info:
            currNode2 = currNode2.right
        else:
            currNode2 = currNode2.left
        v2Path.append(currNode2)


    v1Path.reverse()

    for node in v1Path:
        for node2 in v2Path:
            if node == node2:
                return node

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
