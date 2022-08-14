import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
parent = [0] * n
visited = [False] * n

def bfs(graph, parent, visited):
    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if visited[i] is False:
                parent[i] = pop
                queue.append(i)
                visited[i] = True

bfs(graph, parent, visited)
for i in range(1, len(parent)):
    print(parent[i] + 1)