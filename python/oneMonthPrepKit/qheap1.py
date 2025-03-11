# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

def handleInput():
    queryCount = int(input())
    queries = []
    for _ in range(queryCount):
        queries.append(list(map(int, input().split(' '))))
    return queries
    
    
def execute(queries):
    valueSet = set([])
    heap = []
    heapq.heapify(heap)
    for query in queries:
        if len(query) == 2:
            command, value = query
            if command == 1:
                heapq.heappush(heap,value)
                valueSet.add(value)
            else:
                valueSet.remove(value)
                
        else:
            while heap[0] not in valueSet:
                heapq.heappop(heap)
            print(heap[0])
            
    
queries = handleInput()
execute(queries)