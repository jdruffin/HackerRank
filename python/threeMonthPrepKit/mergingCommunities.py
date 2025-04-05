def find(x):
    while parent[x] != x:
        x = parent[x]
    return x
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if size[x] < size[y]:
        x, y = y, x
    parent[y] = x
    size[x] += size[y]
    
    
n, q = map(int, input().split())

parent = [i for i in range(n+1)]
size   = [1 for _ in range(n+1)]

for _ in range(q):
    query = input().split()
    if query[0] == 'M':
        union(int(query[1]), int(query[2]))       
    else:
        print(size[find(int(query[1]))])