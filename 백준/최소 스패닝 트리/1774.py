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

n, m = map(int, input().split())
location = []
for i in range(n):
    x, y = map(int, input().split())
    location.append([x, y, i])
parent = [i for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    union_parent(parent, x - 1, y - 1)
graph = []
for i in range(n):
    for j in range(i + 1, n):
        graph.append([((location[j][0] - location[i][0]) ** 2 + (location[j][1] - location[i][1]) ** 2) ** (1 / 2), i, j])

graph.sort()
result = []
for i in graph:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        union_parent(parent, i[1], i[2])
        result.append(i[0])

print(format(sum(result), ".2f"))