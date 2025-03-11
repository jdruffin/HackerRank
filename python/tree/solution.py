#!/usr/bin/env python3

def put(adjacencyTree, node1, node2):
    if node1 in adjacencyTree: adjacencyTree[node1].append(node2)
    else: adjacencyTree[node1] = [node2]

def main():
    for currNode in nodesSeen[::-1]: #leaves to root 
        print("currNode" + str(currNode))
        print("first tt" + str(tt))

        r = [tt[adjacentNode] for adjacentNode in adjacencyTree[currNode] if adjacentNode != parent[currNode]] #find potential child of current node that is used in a query
        print("r" + str(r))

        bst = {queryIndex: [getLevel[currNode], currNode, 0] for queryIndex in queries[currNode]} #{queryIndex: currentNodeLevel, currentNodeValue, 0} query -> node info
        print("bst" + str(bst))

        
        if r: #if child of current node is used in a query
            o = max(range(len(r)), key=lambda a: len(r[a]))
            print("o" + str(o))
            print("len(bst)" + str(len(bst)))
            print("len(r[o])" + str(len(r[o])))
            if len(r[o]) > len(bst): r[o], bst = bst, r[o]
        print("second bst" + str(bst))

        ry = {}
        print("second r" + str(r))

        for ae in r:
            for y, v in ae.items():
                put(ry, y, v)
        print("ry" + str(ry))
        for queryIndex, r in ry.items():
            eq, z, t = 0, 0, 0
            if len(r) == 1 and queryIndex not in bst:
                bst[queryIndex] = r[0]
                continue
            if queryIndex in bst: r.append(bst.pop(queryIndex))
            for depth, nodeValue, c in r:
                eq += (depth - getLevel[currNode]) * nodeValue + c
                z += nodeValue
            for depth, nodeValue, c in r:
                c += (depth - getLevel[currNode]) * nodeValue
                diff = (eq - c) * nodeValue
                t += diff
            returns[queryIndex] += t
            bst[queryIndex] = (getLevel[currNode], z, eq)
            # print("returns" + str(returns))
        tt[currNode] = bst
        print("second tt" + str(tt))
        print("")


    # print("returns" + str(returns))


#setting getLevel for all nodes
#setting nodesSeen as an "in order by depth" list
def locate():
    queue = [root]
    level = 0
    while queue:
        level += 1
        tmp = []
        nodesSeen.extend(queue)
        for currentNode in queue:
            for adjacentNode in adjacencyTree[currentNode]:
                if adjacentNode not in parent:
                    parent[adjacentNode] = currentNode
                    getLevel[adjacentNode] = level
                    tmp.append(adjacentNode)
        queue = tmp
    # print(parent)
        

adjacencyTree = {} # {1:[2,3,4], 2:[1], ...}
tt = {} #traversalTree????
numberOfNodes, numberOfQueries = map(int, input().split())
returns = [0] * numberOfQueries

#create adjacency set for all nodes
for _ in range(numberOfNodes - 1):
    node1, node2 = map(int, input().split())
    put(adjacencyTree, node1, node2)
    put(adjacencyTree, node2, node1)

# print(adjacencyTree)

queries = {a: set() for a in adjacencyTree} # node:whichqueries {0:() 1:() 2:(0,2) 3:() 4:(0,2) 5:(1,2) 6:() 7:() 8:()} node -> queries
for y in range(numberOfQueries):
    input()
    for x in map(int, input().split()): queries[x].add(y)

root = next(iter(adjacencyTree))
nodesSeen = []
parent = {root: None}
getLevel = {root: 0}
locate()
main()
# print("returns" + str(returns))
# for s in returns: print(s % (10**9 + 7))