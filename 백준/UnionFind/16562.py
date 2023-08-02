import math
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

n, m, k = map(int, input().split())
costs = list(map(int, input().split()))

parent = [i for i in range(n)]
arr = []
for _ in range(m):
    u, v, = map(int, input().split())
    arr.append([u - 1, v - 1])
    union_parent(parent, u - 1, v - 1)

for i in range(n):
    find_parent(parent, i)

res = 0
for i in set(parent):
    temp = math.inf
    for j, v in enumerate(parent):
        if v == i:
            temp = min(temp, costs[j])
    res += temp

print(res if res <= k else 'Oh no')