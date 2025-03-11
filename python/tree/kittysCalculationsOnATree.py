def put(tree, node1, node2):
    if node1 in tree:
        tree[node1].append(node2)
    else:
        tree[node1] = [node2]


def lca(node1, node2):
    parentList = []
    while node1 != None:
        parentList.append(node1)
        node1 = parents[node1]
    while node2 not in parentList:
        node2 = parents[node2]
    return node2


# parse input
numberOfNodes, numberOfQueries = map(int, input().split())

adjacencyTree = {}
for _ in range(numberOfNodes - 1):
    node1, node2 = map(int, input().split())
    put(adjacencyTree, node1, node2)
    put(adjacencyTree, node2, node1)

queries = {a: set() for a in adjacencyTree}
for y in range(numberOfQueries):
    input()
    for x in map(int, input().split()):
        queries[x].add(y)

# build node list deepest to root
root = next(iter(adjacencyTree))
parents = {root: None}
depths = {root: 0}
nodesByDepth = []
queue = [root]
currDepth = 0
while queue:
    currDepth += 1
    temp = []
    nodesByDepth.extend(queue)
    for currentNode in queue:
        for adjacentNode in adjacencyTree[currentNode]:
            if (adjacentNode not in parents):
                parents[adjacentNode] = currentNode
                depths[adjacentNode] = currDepth
                temp.append(adjacentNode)
    queue = temp

# print(queries)

# calculate LCA and running totals for every combo of nodes
returnValues = [0 for x in range(numberOfQueries)]
currentNodesPerQuery = [[] for x in range(numberOfQueries)]
# priorCalculations = {}
for currNode in nodesByDepth[::-1]:
    if (currNode == 3):
        currNode = 2
    elif(currNode ==2):
        currNode = 3
    print(currNode)
    for query in queries[currNode]:
        # print(query)
        if (len(currentNodesPerQuery[query]) == 0):
            currentNodesPerQuery[query].append(currNode)
            # priorCalculations.update({str(currentNodesPerQuery[query]):
                                    #   [currNode]})
        else:
            latestNodeInQuery = currentNodesPerQuery[query][-1]
            if (len(currentNodesPerQuery[query]) == 1):
                # temp = priorCalculations[str(currentNodesPerQuery[query])]
                # print('str(currentNodesPerQuery[query])' + str(str(currentNodesPerQuery[query])))
                # print('temp1' + str(temp))
                print('currentNodesPerQuery[query]' + str(currentNodesPerQuery[query]))

                newLCA = lca(currNode, latestNodeInQuery)
                print('newLCA' + str(newLCA))

                calc = latestNodeInQuery*currNode * \
                    ((depths[currNode] - depths[newLCA]) +
                     (depths[latestNodeInQuery] - depths[newLCA]))

                currentNodesPerQuery[query].append(currNode)

                # priorCalculations.update({str(currentNodesPerQuery[query]):
                                        #   temp.append(currNode)})
                # print(priorCalculations)
                print(calc)
                returnValues[query] += calc
            else:
                # temp = priorCalculations[str(currentNodesPerQuery[query])]
                # print('temp2' + str(temp))
                # print('str(currentNodesPerQuery[query])' + str(str(currentNodesPerQuery[query])))

                # c1 = sum(temp)
                print('currentNodesPerQuery[query]' + str(currentNodesPerQuery[query]))

                newLCA = lca(currNode, latestNodeInQuery)
                print('newLCA' + str(newLCA))
          
                # print(c1)
                # print(c2)

                # calc = ((c1*(depths[currNode] - depths[newLCA]) + c2)
                #         * currNode) + (currNode*(depths[currNode] - depths[newLCA]))

                # calc = c1 * currNode * (depths[currNode] - depths[newLCA]) + (currNode * c2) #MORE CORRECT
                if(depths[newLCA] <= depths[currNode]):
                    c2 = 0
                    c1 = 0
                    for node in currentNodesPerQuery[query]:
                        c1+= node
                        c2 += node*(depths[node] - depths[newLCA])

                    calc = currNode * (c2 + ((depths[currNode] - depths[newLCA]) * c1))
                    
                    print(calc)
                    returnValues[query] += calc
                else:
                    for node in currentNodesPerQuery[query]:
                        inTree = False
                        while node != newLCA:
                            if(currNode == node):
                                inTree = True
                                break
                            node = parents[node]
                        
                    diff = depths[currNode] - depths[newLCA]
                    calc = currNode * (c2 + ((depths[currNode] - depths[newLCA]) * c1))

                    print(calc)
                    returnValues[query] += calc

                currentNodesPerQuery[query].append(currNode)
                # priorCalculations.update({str(currentNodesPerQuery[query]):
                                        #   temp.append(currNode)})
                # print(calc)

                # returnValues[query] += calc


# print(priorCalculations)

for s in returnValues:
    print(s % (10**9 + 7))
