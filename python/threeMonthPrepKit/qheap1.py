import heapq

def parseInput():
    count = int(input())

    operations = []
    for i in range(count):
        operations.append(list(map(int,input().split(' '))))
    
    return operations

def main(operations):
    heap = []
    hashMap = set()

    for operation in operations:
        if len(operation) == 2:
            if operation[0] == 1:
                heapq.heappush(heap, operation[1])
                hashMap.add(operation[1])
            elif operation[0] == 2:
                hashMap.remove(operation[1])
        else:
            while heap[0] not in hashMap:
                heapq.heappop(heap)
            print(heap[0])

operations = parseInput()
main(operations)