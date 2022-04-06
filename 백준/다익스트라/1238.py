import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
distance = [INF] * (n + 1)

def dijkstra(start):
    heap = []

    heapq.heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, [cost, i[0]])

dijkstra(x)
res_go = distance
for i in range(n):
    distance = [INF] * (n + 1)
    dijkstra(i + 1)
    res_go[i+1] += distance[x]

print(max(res_go[1:]))