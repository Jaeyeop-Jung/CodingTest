# TODO 틀림

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(dp, day):
    if n <= day:
        return 0
    if dp[day] != 0:
        return dp[day]

    cost, score = arr[day]
    if day + cost <= n:
        dp[day] = max(dp[day], dfs(dp, day + cost) + score)
    dp[day] = max(dp[day], dfs(dp, day + 1))
    return dp[day]

dp = [0] * n
print(dfs(dp, 0))