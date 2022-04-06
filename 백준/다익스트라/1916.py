import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
start, destination = map(int, input().split())
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
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, [cost, i[0]])

dijkstra(start)

print(distance[destination])