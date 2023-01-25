import math

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for a in range(n):
            arr[i][j] = min(arr[i][j], arr[i][a] + arr[a][j])

result = math.inf
visited = [False] * n
visited[k] = True
def dfs(visited, now, cost):
    if False not in visited:
        global result
        result = min(result, cost)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(visited, i, cost + arr[now][i])
            visited[i] = False

dfs(visited, k, 0)
print(result)