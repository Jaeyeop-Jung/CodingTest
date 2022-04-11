import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra():
    heap = []
    distance = [INF] * (n + 1)

    heapq.heappush(heap, [0, x])
    distance[x] = 0
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


distance = dijkstra()
if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)
