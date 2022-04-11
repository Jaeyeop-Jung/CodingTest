import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
start, stop = map(int, input().split())

def dijkstra(start):
    heap = []
    distance = [INF] * (n + 1)
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

    return distance, distance_path

distance, distance_path = dijkstra(start)
print(distance[stop])
print(len(distance_path[stop]))
for i in distance_path[stop]:
    print(i, end=" ")