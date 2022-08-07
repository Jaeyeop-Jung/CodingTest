from collections import deque

def dfs(graph, v, visited):
    print(v + 1, end=' ')
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
        print(pop + 1, end=' ')
        for i in graph[pop]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for i in range(len(graph)):
    graph[i].sort()
visited = [False] * n

dfs(graph, v - 1, visited)
print()
visited = [False] * n
bfs(graph, v - 1, visited)
