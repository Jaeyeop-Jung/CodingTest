import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, = map(int, input().split())
height = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, = map(int, input().split())
    if height[a] < height[b]:
        graph[a].append(b)
    elif height[a] > height[b]:
        graph[b].append(a)
    else:
        graph[a].append(b)
        graph[b].append(a)

def dfs(height, graph, dp, cur):
    if not graph[cur]:
        dp[cur] = 1
        return 1
    if dp[cur]:
        return dp[cur]

    for next in graph[cur]:
        dp[cur] = max(dp[cur], dfs(height, graph, dp, next) + 1)
    return dp[cur]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dfs(height, graph, dp, i)

for i in range(1, n + 1):
    print(dp[i])