# TODO 틀림 https://studyandwrite.tistory.com/387

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def dfs(graph, v, visited):
    height = graph[v[0]][v[1]]
    visited[v[0]][v[1]] = True
    if dp[v[0]][v[1]] != 0:
        return dp[v[0]][v[1]]
    if v[0] == n - 1 and v[1] == m - 1:
        return 1

    way = 0
    for i in range(len(dRow)):
        movedRow = v[0] + dRow[i]
        movedColumn = v[1] + dColumn[i]
        if not 0 <= movedRow < n or not 0 <= movedColumn < m:
            continue
        if graph[movedRow][movedColumn] < height and visited[movedRow][movedColumn] is False:
            visited[movedRow][movedColumn] = True
            way += dfs(graph, [movedRow, movedColumn], visited)
            visited[movedRow][movedColumn] = False

    dp[v[0]][v[1]] = way
    return dp[v[0]][v[1]]


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]

print(dfs(graph, [0, 0], visited))