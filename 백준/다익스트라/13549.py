import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(200002)]
for i in range(200002):
    if i - 1 > 0:
        graph[i].append([i - 1, 1])
    if i + 1 < 100001:
        graph[i].append([i + 1, 1])
    if i * 2 < 100001:
        graph[i].append([i * 2, 0])

def dijkstra(start):
    heap = []
    distance = [INF] * (200002)

    heapq.heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, [cost, i[0]])
    return distance

if n < m:
    print(dijkstra(n)[m])
else:
    print(-(m - n))
