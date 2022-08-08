import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000)

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def dfs(graph, v, visited, color):
    visited[v[0]][v[1]] = True
    for i in range(len(dRow)):
        movedRow = v[0] + dRow[i]
        movedColumn = v[1] + dColumn[i]
        if not 0 <= movedRow < n or not 0 <= movedColumn < n:
            continue
        if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] in color:
            dfs(graph, [movedRow, movedColumn], visited, color)

def bfs(graph, v, visited, color):
    queue = deque()
    queue.append(v)

    while queue:
        pop = queue.popleft()
        visited[pop[0]][pop[1]] = True
        for i in range(len(dRow)):
            movedRow = pop[0] + dRow[i]
            movedColumn = pop[1] + dColumn[i]
            if not 0 <= movedRow < n or not 0 <= movedColumn < n:
                continue
            if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] in color:
                queue.append([movedRow, movedColumn])
                visited[movedRow][movedColumn] = True


n = int(input())
graph = [list(input()) for i in range(n)]
colorBlindnessVisited = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

colorBlindnessResult = 0
result = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            # dfs(graph, [i, j], visited, [graph[i][j]])
            bfs(graph, [i, j], visited, [graph[i][j]])
            result += 1
        if colorBlindnessVisited[i][j] is False:
            if graph[i][j] == 'B':
                # dfs(graph, [i, j], colorBlindnessVisited, ['B'])
                bfs(graph, [i, j], colorBlindnessVisited, ['B'])
                colorBlindnessResult += 1
            else:
                # dfs(graph, [i, j], colorBlindnessVisited, ['G', 'R'])
                bfs(graph, [i, j], colorBlindnessVisited, ['G', 'R'])
                colorBlindnessResult += 1

print(result, colorBlindnessResult)