# TODO 틀림 재귀를 잘 생각해봐 좀 여렵다

import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

def dfs(dp, idx):
    if n - 1 == idx:
        return 1
    if dp[idx] != 0:
        return dp[idx]

    dp[idx] = 1
    if idx + 1 <= n:
        dp[idx + 1] = max(dp[idx + 1], dfs(dp, idx + 1))
    for i in range(idx + 1, n):
        if arr[idx] < arr[i]:
            dp[idx] = max(dp[idx], 1 + dfs(dp, i))

    return dp[idx]

dp = [0] * n
dfs(dp, 0)
print(dp)