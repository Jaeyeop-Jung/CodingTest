import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m + 1)]

arr.sort(key=lambda x: -x[2])
minCost = 0
minParent = [i for i in range(n + 1)]
for u, v, w in arr:
    if find_parent(minParent, u) != find_parent(minParent, v):
        union_parent(minParent, u, v)
        if w == 0:
            minCost += 1

arr.sort(key=lambda x: x[2])
maxCost = 0
maxParent = [i for i in range(n + 1)]
for u, v, w in arr:
    if find_parent(maxParent, u) != find_parent(maxParent, v):
        union_parent(maxParent, u, v)
        if w == 0:
            maxCost += 1

print(maxCost ** 2 - minCost ** 2)
