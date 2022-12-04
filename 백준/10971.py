import math
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def dfs(visited, start, cur, cost):
    if False not in visited and arr[cur][start] != 0:
        global result
        result = min(result, cost + arr[cur][start])
        return

    for i in range(len(arr[cur])):
        if not visited[i] and arr[cur][i] != 0:
            visited[i] = True
            dfs(visited, start, i, cost + arr[cur][i])
            visited[i] = False

visited = [False] * n
result = math.inf
for start in range(n):
    for next in range(n):
        if arr[start][next] != 0:
            visited[start] = True
            visited[next] = True
            dfs(visited, start, next, arr[start][next])
            visited[start] = False
            visited[next] = False

print(result)