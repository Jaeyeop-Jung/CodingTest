# TODO 틀림

import math
import sys

input = sys.stdin.readline

n, k, = map(int, input().split())
arr = sorted([list(map(int, input().split())) for _ in range(n)])

def dfs(arr, dp, idx, pre):
    if idx == n:
        return 0
    if dp[idx]:
        return dp[idx]

    dp[idx] = max(dp[idx], dfs(arr, dp, idx + 1, pre))
    next = bisect_left(temp, arr[idx][0] + k)
    dp[idx] = max(dp[idx], dfs(arr, dp, next, arr[idx][0]) + arr[idx][1])
    return dp[idx]


dp = [0] * n
temp = [i[0] for i in arr]
print(dfs(arr, dp, 0, -math.inf))