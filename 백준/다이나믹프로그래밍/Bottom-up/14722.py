# TODO 틀림

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

if arr[0][0] == 0:
    dp[0][0][arr[0][0]] = 1
for r in range(n):
    for c in range(n):
        if 0 <= r - 1 < n:
            dp[r][c][0] = max(dp[r][c][0], dp[r - 1][c][0])
            dp[r][c][1] = max(dp[r][c][1], dp[r - 1][c][1])
            dp[r][c][2] = max(dp[r][c][2], dp[r - 1][c][2])
            if arr[r][c] != 1 or (arr[r][c] == 1 and dp[r - 1][c] != 0):
                dp[r][c][arr[r][c]] = max(dp[r][c][arr[r][c]], dp[r - 1][c][(arr[r][c] - 1) % 3] + 1)
        if 0 <= c - 1 < n:
            dp[r][c][0] = max(dp[r][c][0], dp[r][c - 1][0])
            dp[r][c][1] = max(dp[r][c][1], dp[r][c - 1][1])
            dp[r][c][2] = max(dp[r][c][2], dp[r][c - 1][2])
            if arr[r][c] != 1 or (arr[r][c] == 1 and dp[r][c - 1] != 0):
                dp[r][c][arr[r][c]] = max(dp[r][c][arr[r][c]], dp[r][c - 1][(arr[r][c] - 1) % 3] + 1)

print(max(dp[-1][-1]))