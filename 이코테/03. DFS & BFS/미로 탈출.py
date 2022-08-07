from collections import deque

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def bfs(graph, result, visited):
    queue = deque()
    queue.append([0, 0])
    result[0][0] = 1
    while queue:
        pop = queue.popleft()
        visited[pop[0]][pop[1]] = True
        for i in range(len(dRow)):
            curRow = dRow[i] + pop[0]
            curColumn = dColumn[i] + pop[1]
            if curRow == n - 1 and curColumn == m - 1:
                return result[pop[0]][pop[1]] + 1
            if (not 0 <= curRow < n) or (not 0 <= curColumn < m):
                continue
            if visited[curRow][curColumn] is False and graph[curRow][curColumn] == 1:
                queue.append([curRow, curColumn])
                result[curRow][curColumn] = result[pop[0]][pop[1]] + 1

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
visited = [[False] * m for i in range(n)]
result = [[0] * m for i in range(n)]

print(bfs(arr, result, visited))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111