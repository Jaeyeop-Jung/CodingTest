import math
import sys
from collections import deque

input = sys.stdin.readline

n, m, a, b, c, = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

q = deque()
q.append([a - 1, 0, 0])
visited = [[False] * (c + 1) for _ in range(n)]
visited[a - 1][0] = True
res = math.inf
while q:
    cur, curCost, maxCost, = q.popleft()
    if cur == b - 1:
        res = min(res, maxCost)
        continue
    for next, cost in graph[cur]:
        nextCost = cost + curCost
        if c < nextCost or visited[next][nextCost]:
            continue
        visited[next][nextCost] = True
        q.append([next, nextCost, max(maxCost, cost)])

print(res if res != math.inf else -1)