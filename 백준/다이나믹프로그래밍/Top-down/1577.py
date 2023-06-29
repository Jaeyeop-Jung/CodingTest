import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, = map(int, input().split())
k = int(input())
fixRoad = defaultdict(set)
for _ in range(k):
    a, b, c, d = map(int, input().split())
    fixRoad[(a, b)].add((c, d))
    fixRoad[(c, d)].add((a, b))

def dfs(dp, fixRoad, r, c):
    if r == n and c == m:
        return 1
    if n < r or m < c:
        return 0
    if dp[r][c] != 0:
        return dp[r][c]


    if (r + 1, c) not in fixRoad[(r, c)]:
        dp[r][c] += dfs(dp, fixRoad, r + 1, c)
    if (r, c + 1) not in fixRoad[(r, c)]:
        dp[r][c] += dfs(dp, fixRoad, r, c + 1)
    return dp[r][c]

dp = [[0] * (m + 1) for _ in range(n + 1)]
print(dfs(dp, fixRoad, 0, 0))
print()