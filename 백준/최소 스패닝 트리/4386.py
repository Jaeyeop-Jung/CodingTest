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

n = int(input())
star = [[0.0, 0.0]]
for i in range(n):
    a, b = map(float, input().split())
    star.append([a, b])
parent = []
for i in range(n + 1):
    parent.append(i)

graph = []
for i in range(1, n + 1):
    for j in range(i + 1, n+1):
        distance = round(((star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2) ** (1 / 2), 2)
        graph.append([distance, i, j])

graph.sort()
result = 0.0
for i in graph:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        union_parent(parent, i[1], i[2])
        result += i[0]

print(result)