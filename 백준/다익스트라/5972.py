import math
import sys
import heapq

input = sys.stdin.readline

n, m, = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])
    graph[b - 1].append([a - 1, c])

distance = [math.inf] * n
distance[0] = 0
h = [[0, 0]]
while h:
    dist, cur, = heapq.heappop(h)
    if distance[cur] < dist:
        continue
    for next, cost in graph[cur]:
        total = dist + cost
        if total < distance[next]:
            heapq.heappush(h, [total, next])
            distance[next] = total

print(distance[-1])