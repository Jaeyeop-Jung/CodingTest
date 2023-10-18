
n = int(input())
start = [int(input()) for _ in range(n)]
graph = []
for u in range(n):
    temp = list(map(int, input().split()))
    for v in range(n):
        if u == v:
            continue
        graph.append((u + 1, v + 1, temp[v]))
for i in range(n):
    graph.append((0, i + 1, start[i]))
graph.sort(key=lambda x: x[-1])

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

parent = [i for i in range(n + 1)]
res = 0
for u, v, w in graph:
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        res += w

print(res)
