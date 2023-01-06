# TODO 할 수 있다

import math
import sys
from collections import deque
input = sys.stdin.readline

n, m, = map(int, input().split())
graph = [[] for _ in range(n + 1)]
start, end = math.inf, 0
for i in range(m):
    a, b, c, = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    start = min(start, c)
    end = max(end, c)
u, v = map(int, input().split())

def bfs(w):
    q = deque()
    q.append(u)
    visited = [False] * (n + 1)
    visited[u] = True
    while q:
        cur = q.popleft()
        for dest, dist in graph[cur]:
            if visited[dest] or dist <= w:
                continue
            q.append(dest)
            visited[dest] = True
    if visited[v]:
        return True
    return False

while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        start = mid + 1
    else:
        end = mid - 1

print(start)