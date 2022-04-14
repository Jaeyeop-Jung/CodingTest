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

v, e = map(int, input().split())
graph = []
for i in range(e):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

graph.sort()
result = 0
for i in graph:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        union_parent(parent, i[1], i[2])
        result += i[0]

print(result)
