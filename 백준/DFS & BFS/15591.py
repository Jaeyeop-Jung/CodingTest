import math
import sys
from collections import deque

input = sys.stdin.readline

n, q, = map(int, input().split())
graph = [[] for _ in range(n)]
board = [[math.inf] * n for _ in range(n)]
for i in range(n - 1):
    u, v, r = map(int, input().split())
    graph[u - 1].append([v - 1, r])
    graph[v - 1].append([u - 1, r])
query = [list(map(int, input().split())) for _ in range(q)]

for i in range(n):
    q = deque()
    visited = [False] * n
    visited[i] = True
    for next in graph[i]:
        q.append(next)
        visited[next[0]] = True
        board[i][next[0]] = next[1]
    while q:
        next, cost, = q.popleft()
        for nextNode, nextCost in graph[next]:
            if not visited[nextNode]:
                visited[nextNode] = True
                q.append([nextNode, min(cost, nextCost)])
                board[i][nextNode] = min(cost, nextCost)

for k, v in query:
    cnt = 0
    for usado in board[v - 1]:
        if k <= usado and usado != math.inf:
            cnt += 1
    print(cnt)
