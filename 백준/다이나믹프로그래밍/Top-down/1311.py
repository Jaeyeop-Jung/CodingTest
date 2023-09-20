import math

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(arr, dp, idx, visit):
    if idx == n:
        return 0
    if visit in dp[idx]:
        return dp[idx][visit]

    dp[idx][visit] = math.inf
    for i in range(n):
        if visit & 1 << i == 0:
            dp[idx][visit] = min(
                dp[idx][visit],
                dfs(arr, dp, idx + 1, visit | 1 << i) + arr[idx][i]
            )

    return dp[idx][visit]

dp = [{} for _ in range(n)]
print(dfs(arr, dp, 0, 0))