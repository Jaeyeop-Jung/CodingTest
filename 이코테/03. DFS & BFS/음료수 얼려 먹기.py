
# 00110
# 00011
# 11111
# 00000

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

arr = []
for i in range(4):
    arr.append(list(map(int, input())))

count = 0
def dfs(graph, v, visited):
    visited[v[0]][v[1]] = True
    for i in range(4):
        curRow = v[0] + dRow[i]
        curColumn = v[1] + dColumn[i]
        if (not 0 <= curRow <= 3) or (not 0 <= curColumn <= 4):
            continue
        if graph[curRow][curColumn] == 0 and visited[curRow][curColumn] is False:
            dfs(graph, [curRow, curColumn], visited)


visited = [[False] * 5 for _ in range(4)]
for i in range(len(visited)):
    for j in range(len(visited[i])):
        if visited[i][j] is False and arr[i][j] == 0:
            count += 1
            dfs(arr, [i, j], visited)

print(count)