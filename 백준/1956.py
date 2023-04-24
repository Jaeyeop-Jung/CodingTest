# TODO 틀림

import heapq
import math
import sys

input = sys.stdin.readline

v, e, = map(int, input().split())
graph = [[] for _ in range(v)]
for _ in range(e):
    a, b, c, = map(int, input().split())
    graph[a - 1].append([b - 1, c])

def dijkstra(start):
    distance = [math.inf] * v
    h = [[0, start]]
    distance[start] = 0
    while h:
        cost, cur, = heapq.heappop(h)
        if distance[cur] < cost:
            continue
        for next, dist in graph[cur]:
            totalCost = dist + cost
            if totalCost < distance[next]:
                heapq.heappush(h, [totalCost, next])
                distance[next] = totalCost
    return distance

distance = []
for i in range(v):
    distance.append(dijkstra(i))

result = math.inf
for cur in range(v):
    for next in range(v):
        if cur != next:
            result = min(result, distance[cur][next] + distance[next][cur])

print(result if result != math.inf else -1)