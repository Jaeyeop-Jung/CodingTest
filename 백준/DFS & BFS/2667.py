
dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def dfs(graph, count, v, visited):
    visited[v[0]][v[1]] = True
    graph[v[0]][v[1]] = count
    for i in range(len(dRow)):
        movedRow = v[0] + dRow[i]
        movedColumn = v[1] + dColumn[i]
        if not 0 <= movedRow < n or not 0 <= movedColumn < n:
            continue
        if visited[movedRow][movedColumn] is False and graph[movedRow][movedColumn] == 1:
            dfs(graph, count, [movedRow, movedColumn], visited)


n = int(input())
graph = [list(map(int, input())) for i in range(n)]
visited = [[False] * n for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] is False and graph[i][j] == 1:
            count += 1
            dfs(graph, count, [i, j], visited)

print(count)
result = [0] * count
for i in range(1, count + 1):
    for j in range(len(graph)):
        result[i - 1] += graph[j].count(i)
result.sort()
for i in result:
    print(i)

