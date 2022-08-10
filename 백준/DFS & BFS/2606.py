from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] is False:
            visited[i] = True
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)

    while queue:
        pop = queue.popleft()
        visited[pop] = True
        for i in graph[pop]:
            if visited[i] is False:
                visited[i] = True
                queue.append(i)

n = int(input())
m = int(input())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
visited = [False] * n

dfs(graph, 0, visited)
print(visited.count(True) - 1)

#
# visited = [False] * n
# bfs(graph, 0, visited)
# print(visited.count(True) - 1)