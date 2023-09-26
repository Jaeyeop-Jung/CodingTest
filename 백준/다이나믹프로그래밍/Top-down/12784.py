import math
import sys

input = sys.stdin.readline

def dfs(graph, dp, visited, cur, pre):
    visited[cur] = True
    dp[cur] = 0
    for next, cost in graph[cur]:
        if not visited[next]:
            dp[cur] += dfs(graph, dp, visited, next, cost)
    if dp[cur] == 0:
        dp[cur] = pre
    else:
        dp[cur] = min(dp[cur], pre)
    return dp[cur]

t = int(input())
for _ in range(t):
    n, m, = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    dp = [math.inf] * (n + 1)
    visited = [False] * (n + 1)
    res = dfs(graph, dp, visited, 1, math.inf)
    print(res if res != math.inf else 0)