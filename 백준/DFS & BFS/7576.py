# TODO 틀림

from collections import deque

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

m, n = map(int, input().split())
graph = []
start = []
tomatify = [[-1] * m for i in range(n)]
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(len(inp)):
        if inp[j] == 1:
            start.append([i, j])
            tomatify[i][j] = 0
        elif inp[j] == -1:
            tomatify[i][j] = -2
    graph.append(inp)

def bfs(tomatify, row, column, visited):
    queue = deque()
    queue.append([row, column])

    while queue:
        popRow, popColumn = queue.popleft()
        visited[popRow][popColumn] = True
        for i in range(len(dRow)):
            movedRow = popRow + dRow[i]
            movedColumn = popColumn + dColumn[i]
            if not 0 <= movedRow < n or not 0 <= movedColumn < m:
                continue
            if graph[movedRow][movedColumn] == -1 or graph[movedRow][movedColumn] == 1 or visited[movedRow][movedColumn]:
                continue
            if graph[movedRow][movedColumn] == 0:
                visited[movedRow][movedColumn] = True
                queue.append([movedRow, movedColumn])
                if tomatify[movedRow][movedColumn] != -1:
                    tomatify[movedRow][movedColumn] = min(tomatify[movedRow][movedColumn], tomatify[popRow][popColumn] + 1)
                else:
                    tomatify[movedRow][movedColumn] = tomatify[popRow][popColumn] + 1

for i in start:
    visited = [[False] * m for _ in range(n)]
    bfs(tomatify, i[0], i[1], visited)

result = -1
for i in tomatify:
    for j in i:
        if j == -1:
            print(-1)
            exit(0)
        result = max(result, j)
print(result)
