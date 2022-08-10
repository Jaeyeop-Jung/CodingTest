import sys
from collections import deque

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

# def dfs(graph, v, visited):
#     visited[v[0]][v[1]] = True
#     for i in range(len(dRow)):
#         movedRow = v[0] + dRow[i]
#         movedColumn = v[1] + dColumn[i]
#         if not 0 <= movedRow < m or not 0 <= movedColumn < n:
#             continue
#         if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] == 1:
#             dfs(graph, [movedRow, movedColumn], visited)

# def dfs(graph, v, visited):
#     stack = []
#     stack.append(v)
#     while stack:
#         pop = stack.pop()
#         for i in range(len(dRow)):
#             movedRow = pop[0] + dRow[i]
#             movedColumn = pop[1] + dColumn[i]
#             if not 0 <= movedRow < m or not 0 <= movedColumn < n:
#                 continue
#             if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] == 1:
#                 visited[movedRow][movedColumn] = True
#                 stack.append([movedRow, movedColumn])

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)

    while queue:
        pop = queue.popleft()
        visited[pop[0]][pop[1]] = True
        for i in range(len(dRow)):
            movedRow = pop[0] + dRow[i]
            movedColumn = pop[1] + dColumn[i]
            if not 0 <= movedRow < m or not 0 <= movedColumn < n:
                continue
            if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] == 1:
                visited[movedRow][movedColumn] = True
                queue.append([movedRow, movedColumn])


t = int(input())
for _ in range(t):
    n, m, k, = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    visited = [[False] * n for _ in range(m)]

    result = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1 and visited[i][j] is False:
                bfs(graph, [i, j], visited)
                result += 1

    print(result)
