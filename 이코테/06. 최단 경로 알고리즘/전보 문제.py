import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])

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
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, [cost, i[0]])


    return distance


distance = dijkstra(c)
cnt = 0
max_distance = 0
for i in distance:
    if i < INF:
        cnt += 1
        max_distance = max(max_distance, i)

print(cnt - 1, max_distance)
