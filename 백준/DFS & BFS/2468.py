import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def dfs(height, graph, v, visited):
    visited[v[0]][v[1]] = True
    for i in range(len(dRow)):
        movedRow = v[0] + dRow[i]
        movedColumn = v[1] + dColumn[i]
        if not 0 <= movedRow < n or not 0 <= movedColumn < n:
            continue
        if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] > height:
            dfs(height, graph, [movedRow, movedColumn], visited)

def bfs(height, graph, v, visited):
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
            if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] > height:
                queue.append([movedRow, movedColumn])
                visited[movedRow][movedColumn] = True

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
maxHigh = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        maxHigh = max(maxHigh, graph[i][j])

result = 0
for i in range(maxHigh):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for j in range(len(graph)):
        for k in range(len(graph[j])):
            if visited[j][k] is False and graph[j][k] > i:
                # dfs(i, graph, [j, k], visited)
                bfs(i, graph, [j, k], visited)
                count += 1
    result = max(result, count)

print(result)