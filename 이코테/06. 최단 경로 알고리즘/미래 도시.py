import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
x, k = map(int, input().split())


def dijkstra(start):
    heap = []
    distance = [INF] * (n + 1)

    heapq.heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(heap, [cost, i])

    return distance


cost = dijkstra(1)[k] + dijkstra(k)[x]
if cost >= INF:
    print(-1)
else:
    print(cost)
