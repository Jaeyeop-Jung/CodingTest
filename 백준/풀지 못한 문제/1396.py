import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parnet(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def dijkstra(start):
    heap = []
    distance = [INF] * (n + 1)
    graph = [[] for i in range(n + 1)]
    for i in edges:
        graph[i[1]].append([i[2], i[1]])
    distance_path = [[] for i in range(n + 1)]

    heapq.heappush(heap, [0, start, [start]])
    distance[start] = 0
    while heap:
        dist, now, path = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                distance_path[i[0]] = path + [i[0]]
                heapq.heappush(heap, [cost, i[0], distance_path[i[0]]])
    return distance_path

n, m = map(int, input().split())
edges = []
edges2 = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
    edges.append([c, b, a])
    edges2[a][b] = c
    edges2[b][a] = c
q = int(input())
query = []
for i in range(q):
    a, b = map(int, input().split())
    query.append([a, b])
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parnet(parent, a, b)

for i in range(n + 1):
    find_parent(parent, i)

for i in query:
    if parent[i[0]] != parent[i[1]]:
        print(-1)
    else:
        start_parent = parent[i[0]]
        same_parent = []
        for j in range(len(parent)):
            if parent[j] == start_parent:
                same_parent.append(j)

        max_cost = 0
        path = dijkstra(i[0])
        for j in range(len(path[i[1]]) - 1):
            max_cost = max(max_cost, edges2[path[i[1]][j]][path[i[1]][j + 1]])

        path_num = []
        for j in path[i[1]]:
            for k in range(len(edges2[j])):
                if edges2[j][k] != 0 and edges2[j][k] <= max_cost:
                    path_num.append(k)
        print(max_cost, len(list(set(path_num))))
