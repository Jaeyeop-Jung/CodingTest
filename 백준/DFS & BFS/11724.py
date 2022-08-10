from collections import deque
import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] is False:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)

    while queue:
        pop = queue.popleft()
        visited[pop] = True
        for i in graph[pop]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph = [[] * m for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
visited = [False] * n

result = 0
for i in range(n):
    if visited[i] is False:
        # dfs(graph, i, visited)
        bfs(graph, i, visited)
        result += 1

print(result)