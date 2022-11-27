# TODO 틀림

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0] * (m + 1) for i in range(n + 1)]
for r in range(1, n + 1):
    for c in range(1, m + 1):
        dp[r][c] = arr[r-1][c-1] + dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1]

k = int(input())
for case in range(k):
    i, j, x, y = map(int, input().split())
    result = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]
    print(result)