import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

dRow = [0, 0, 1, -1, -1, 1, 1, -1]
dColumn = [1, -1, 0, 0, 1, 1, -1, -1]

def dfs(graph, v, visited):
    visited[v[0]][v[1]] = True
    for i in range(len(dRow)):
        movedRow = v[0] + dRow[i]
        movedColumn = v[1] + dColumn[i]
        if not 0 <= movedRow < h or not 0 <= movedColumn < w:
            continue
        if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] == 1:
            dfs(graph, [movedRow, movedColumn], visited)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [[] * w for i in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().split()))
    visited = [[False] * w for i in range(h)]
    result = 0

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if visited[i][j] is False and graph[i][j] == 1:
                dfs(graph, [i, j], visited)
                result += 1
    print(result)


