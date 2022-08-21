# DFS로는 시간초과가 떠서 안된다!

import math
import sys
from collections import deque

sys.setrecursionlimit(10000)

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [[False] * m for i in range(n)]

result = math.inf

# def dfs(graph, v, visited, cnt):
#     visited[v[0]][v[1]] = True
#     for i in range(len(dRow)):
#         movedRow = v[0] + dRow[i]
#         movedColumn = v[1] + dColumn[i]
#         if movedRow == n - 1 and movedColumn == m - 1:
#             global result
#             result = min(result, cnt + 1)
#         if not 0 <= movedRow < n or not 0 <= movedColumn < m:
#             continue
#         if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] == 1:
#             dfs(graph, [movedRow, movedColumn], visited, cnt + 1)
#             visited[movedRow][movedColumn] = False
# dfs(graph, [0, 0], visited, 1)

cnt = 1
def bfs(graph, v, visited):
    queue = deque()
    queue.append([v[0], v[1], cnt])

    while queue:
        row, column, localCnt = queue.popleft()
        visited[row][column] = True
        for i in range(len(dRow)):
            movedRow = row + dRow[i]
            movedColumn = column + dColumn[i]
            if movedRow == n - 1 and movedColumn == m - 1:
                global result
                result = min(result, localCnt + 1)
            if not 0 <= movedRow < n or not 0 <= movedColumn < m:
                continue
            if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] == 1:
                visited[movedRow][movedColumn] = True
                queue.append([movedRow, movedColumn, localCnt + 1])
bfs(graph, [0, 0], visited)

print(result)
