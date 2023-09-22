import math
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        degree[a] += 1
        degree[b] += 1

    q = deque()
    costs = [math.inf] * (n + 1)
    for i in range(2, n + 1):
        if len(graph[i]) == 1:
            q.append(i)

    while q:
        cur = q.popleft()
        for next, cost in graph[cur]:
            if costs[next] == math.inf:
                costs[next] = 0
            degree[next] -= 1
            costs[next] += min(costs[cur], cost)
            graph[next].remove((cur, cost))
            if degree[next] == 1 and next != 1:
                q.append(next)

    print(costs[1] if costs[1] != math.inf else 0)
