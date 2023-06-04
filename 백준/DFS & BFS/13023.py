import math
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# def bfs(start):
#     visited = [math.inf] * n
#     visited[start] = 0
#     q = deque()
#     q.append([start, 0])
#     while q:
#         cur, cnt = q.popleft()
#         for next in graph[cur]:
#             if visited[next] != math.inf:
#                 continue
#             visited[next] = cnt + 1
#             q.append([next, cnt + 1])
#     max1 = max(visited)
#     fars = [i for i, v in enumerate(visited) if v == max1]
#     return max1, fars


# _, fars, = bfs(0)
# maxDist = 0
# for far in fars:
#     tempMax, _, = bfs(far)
#     maxDist = max(maxDist, tempMax)
# if 3 <= maxDist:
#     print(1)
# else:
#     print(0)

def dfs(graph, visited, cur, cnt):
    if cnt == 5:
        print(1)
        exit()
    for next in graph[cur]:
        if not visited[next]:
            visited[next] = True
            dfs(graph, visited, next, cnt + 1)
            visited[next] = False

visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs(graph, visited, i, 1)
    visited[i] = False

print(0)