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
star = []
for i in range(n):
    x, y, z = map(int, input().split())
    star.append([x, y, z, i])
parent = []
for i in range(n):
    parent.append(i)

graph = []
for i in range(3):
    star.sort(key=lambda x:x[i])
    for j in range(n - 1):
        graph.append([abs(star[j][i] - star[j + 1][i]), star[j][3], star[j + 1][3]])

graph.sort()
result = 0
for i in graph:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        union_parent(parent, i[1], i[2])
        result += i[0]

print(result)

