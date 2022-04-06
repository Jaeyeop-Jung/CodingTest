import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    heap = []

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

case1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n]
case2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]

res = min(case1, case2)
if res >= INF:
    print(-1)
else:
    print(res)
