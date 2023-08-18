import math
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    u, v, w, = map(int, input().split())
    if (arr[u] == 1 and u != n - 1) or (arr[v] == 1 and v != n - 1):
        continue
    graph[u].append((v, w))
    graph[v].append((u, w))

h = [[0, 0]]
distance = [math.inf] * n
distance[0] = 0
while h:
    cost, cur, = heapq.heappop(h)

    if distance[cur] < cost:
        continue

    for next, dist in graph[cur]:
        totalCost = cost + dist
        if totalCost < distance[next]:
            distance[next] = totalCost
            heapq.heappush(h, [totalCost, next])

print(distance[-1] if distance[-1] != math.inf else -1)