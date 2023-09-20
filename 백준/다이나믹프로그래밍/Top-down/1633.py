import math


def dfs(arr, dp, idx, l, r):
    if idx == len(arr):
        if l + r != 30:
            return -math.inf
        return 0
    if dp[idx][l][r] != -1:
        return dp[idx][l][r]

    if l < 15:
        dp[idx][l][r] = max(dp[idx][l][r], dfs(arr, dp, idx + 1, l + 1, r) + arr[idx][0])
    if r < 15:
        dp[idx][l][r] = max(dp[idx][l][r], dfs(arr, dp, idx + 1, l, r + 1) + arr[idx][1])
    dp[idx][l][r] = max(dp[idx][l][r], dfs(arr, dp, idx + 1, l, r))
    return dp[idx][l][r]

arr = []
while True:
    try:
        l = list(map(int, input().split()))
        arr.append(l)
    except:
        break

dp = [[[-1] * 16 for _ in range(16)] for _ in range(len(arr))]
print(dfs(arr, dp, 0, 0, 0))